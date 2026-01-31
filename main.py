import os
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, END, START

# Load environment variables
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# Define the State
class AgentState(TypedDict):
    messages: List[BaseMessage]
    product: str
    availability_checked: bool
    order_placed: bool

def agent_node(state: AgentState):
    """
    Core logic to decide what to say based on the conversation history.
    """
    messages = state["messages"]
    if not messages:
        return {"messages": [AIMessage(content="How can I help you with your order?")]}
        
    last_user_message = messages[-1].content.lower()
    
    # 1. Check Product availability stage
    if not state["availability_checked"]:
        # Simple keywords for demo - in real life LLM would extract product
        system_prompt = (
            "The user might be asking for a product. "
            "If they specify a product name, reply only with 'Yes, [product] is available.' "
            "Be extremely concise. 1 sentence max."
        )
        response = llm.invoke([SystemMessage(content=system_prompt)] + messages)
        
        # Update state if it looks like a confirmation
        is_available = "available" in response.content.lower() or "yes" in response.content.lower()
        return {
            "messages": [response],
            "availability_checked": is_available
        }
    
    # 2. Order placement stage
    elif state["availability_checked"] and not state["order_placed"]:
        system_prompt = (
            "The user previously checked a product. Now they might want to order. "
            "If they confirm the order, reply with 'Order completed successfully. Thank you!' "
            "Otherwise, ask for order details like quantity. 1 sentence max."
        )
        response = llm.invoke([SystemMessage(content=system_prompt)] + messages)
        
        is_placed = "completed" in response.content.lower() or "successfully" in response.content.lower()
        return {
            "messages": [response],
            "order_placed": is_placed
        }
    
    # 3. Final fallback
    else:
        return {"messages": [AIMessage(content="Thank you for your order!")]}

# Define the Graph
workflow = StateGraph(AgentState)
workflow.add_node("agent", agent_node)
workflow.add_edge(START, "agent")
workflow.add_edge("agent", END)

app = workflow.compile()

if __name__ == "__main__":
    print("\nInteractive Order Agent")
    print("----------------------------------------")
    print("Type your message (e.g., 'Do you have Wireless Mice?')")
    
    state = {
        "messages": [],
        "product": "",
        "availability_checked": False,
        "order_placed": False
    }
    
    while not state["order_placed"]:
        user_input = input("\nYou: ").strip() # Strip whitespace
        
        if not user_input: # Skip empty input
            continue
            
        if user_input.lower() in ["exit", "quit"]:
            break
            
        state["messages"].append(HumanMessage(content=user_input))
        
        try:
            # Running the graph
            result = app.invoke(state)
            
            # Update state with result entries
            state.update({k: v for k, v in result.items() if k != "messages"})
            # Append only the new AI message to state messages
            state["messages"].append(result["messages"][-1])
            
            print(f"Agent: {result['messages'][-1].content}")
            
        except Exception as e:
            if "quota" in str(e).lower() or "429" in str(e):
                # Manual Fallback for quota issues to demonstrate the flow
                if not state["availability_checked"]:
                    reply = "Yes, that product is available."
                    state["availability_checked"] = True
                else:
                    reply = "Order completed successfully. Thank you!"
                    state["order_placed"] = True
                print(f"Agent (Fallback): {reply}")
            else:
                print(f"Error: {e}")
                break
    
    print("\n----------------------------------------")
    print("Goodbye!")

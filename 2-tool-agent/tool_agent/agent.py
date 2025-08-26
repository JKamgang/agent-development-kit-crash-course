# from google.adk.agents import Agent
# # from google.adk.tools import google_search
# # 20240824 -- to fix datetime is not defined
# # Curation - by Jean Baptiste
# from datetime import datetime
# from google.adk.tools import google_search, FunctionTool

# get_current_time_tool = FunctionTool(
#     name="get_current_time",
#     description="Returns the current time in YYYY-MM-DD HH:MM:SS format",
#     func=get_current_time,
# )
# 
# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }
# 
# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Tool agent",
#     instruction="""
#     You are a helpful assistant that can use the following tools:
#     - get_current_time
#     - google_search
#     """,
#     tools=[google_search, get_current_time_tool],
# )


# # root_agent = Agent(
# #     name="tool_agent",
# #     model="gemini-2.0-flash",
# #     description="Tool agent",
# #     instruction="""
# #     You are a helpful assistant that can use the following tools:
# #     - get_current_time 
# #     """,
# #     # tools=[google_search],
# #     tools=[get_current_time],
# #     # tools=[google_search, get_current_time], # <--- Doesn't work
# # )
# from google.adk.agents import Agent
# from google.adk.tools import google_search, FunctionTool
# from datetime import datetime

# # 🛠️ Custom tool: Get current time
# def get_current_time() -> dict:
#     """
#     Returns the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

# # 🧠 Wrap the function as an ADK-compatible tool
# get_current_time_tool = FunctionTool(
#     name="get_current_time",
#     description="Returns the current time in YYYY-MM-DD HH:MM:SS format",
#     func=get_current_time,
#     parameters={
#         "type": "object",
#         "properties": {},
#         "required": []
#     }
# )

# 20250825 -- fixed import of FunctionTool
# Jean Baptiste


# from google.adk.tools import FunctionTool
# from datetime import datetime

# def get_current_time() -> dict:
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

# get_current_time_tool = FunctionTool.from_function(
#     func=get_current_time,
#     description="Returns the current time in YYYY-MM-DD HH:MM:SS format",
#     parameters={
#         "type": "object",
#         "properties": {},
#         "required": []
#     }
# )

# # 🤖 Define the agent
# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Tool agent that can perform time lookup and web search",
#     instruction="""
#     You are a helpful assistant that can use the following tools:
#     - get_current_time: returns the current time
#     - google_search: performs a web search
#     """,
#     tools=[google_search, get_current_time_tool],
# )

# ChatGPT

# from google.adk.agents import Agent
# from google.adk.tools import google_search, FunctionTool
# from datetime import datetime

# # 🛠️ Custom tool: Get current time
# def get_current_time() -> dict:
#     """
#     Returns the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

# # 🧠 Wrap the function as an ADK-compatible tool
# get_current_time_tool = FunctionTool(
#     name="get_current_time",
#     description="Returns the current time in YYYY-MM-DD HH:MM:SS format",
#     func=get_current_time,
#     parameters={
#         "type": "object",
#         "properties": {},  # no arguments needed
#         "required": []
#     }
# )

# # 🤖 Define the agent
# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Tool agent that can perform time lookup and web search",
#     instruction="""
#         You are a helpful assistant that can use the following tools:
#         - get_current_time: returns the current time
#         - google_search: performs a web search
#     """,
#     tools=[google_search, get_current_time_tool],
# )

# # Example: use the agent
# if __name__ == "__main__":
#     response = root_agent.run("What time is it now?")
#     print(response)

# # ChatGPT
# from google.adk.agents import Agent
# from google.adk.tools import google_search
# from datetime import datetime

# def get_current_time() -> dict:
#     """
#     Returns the current time in YYYY-MM-DD HH:MM:SS format
#     """
#     return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Time + search agent",
#     instruction="Use tools as needed",
#     tools=[google_search, get_current_time],
# )


# Very simple example with only one tool 
# Very good for understanding the basics -- working using the function directly to get time
#     Google search is commented out to avoid confusion -- - and the first script was working too,

# # Curation - by Jean Baptiste
# #    



# from google.adk.agents import Agent
# from datetime import datetime

# # 🛠️ Tool: get_current_time
# def get_current_time() -> dict:
#     """
#     Returns the current time in YYYY-MM-DD HH:MM:SS format
#     """
#     return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

# # 🤖 Define the agent
# root_agent = Agent(
#     name="time_agent",
#     model="gemini-2.0-flash",
#     description="Agent that returns the current time",
#     instruction="""
#     You are a helpful assistant. You can use the 'get_current_time' tool
#     to return the current date and time in YYYY-MM-DD HH:MM:SS format.
#     """,
#     tools=[get_current_time],  # only the current time tool
# )


# # Example usage 2 tools in one agent
# # 20250825 - Jean Baptiste
# # -- Curation
# # --  attempts to have both tools working in one agent get_current_time and add_numbers

# ChatGPT version working very well

# # file: tool_agent/agent.py
# from datetime import datetime
# #from google.adk.agents import Agent

# from google.adk.agents import Agent
# def get_current_time() -> dict:
#     """
#     Returns the current time in YYYY-MM-DD HH:MM:SS format
#     """
#     return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

# def add_numbers(a: int, b: int) -> dict:
#     """
#     Adds two integers and returns their sum.
#     Args:
#       a: first integer
#       b: second integer
#     """
#     return {"sum": a + b}

# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",  # works for function tools
#     description="Demo agent with two tools",
#     instruction="""
#         You are a helpful assistant. When the user asks for time and a calculation,
#         call BOTH tools in sequence and include their results in one final answer.
#         - Use 'get_current_time' to get the current time.
#         - Use 'add_numbers' when the user asks to add two integers.
#     """,
#     tools=[get_current_time, add_numbers],
# )

# if __name__ == "__main__":
#     # A prompt that strongly encourages calling both tools
#     prompt = "First tell me the current time, then add 2 and 3."
#     print(root_agent.run(prompt))


# This my own design expanded to 5 tools
# # file: tool_agent/agent.py
# by Jean Baptiste
# 20250825
# # -- Curation


# # Microsoft 1st attempt to have 5 tools in one agent
# # Issue with import of FunctionTool not fixed: AttributeError: type object 'FunctionTool' has no attribute 'from_function'
# # INFO:     127.0.0.1:43830 - "

# from datetime import datetime
# from google.adk.agents import Agent
# from google.adk.tools import google_search, FunctionTool

# # 🕒 Tool 1: Get current time
# def get_current_time() -> dict:
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }

# # ➕ Tool 2: Add two numbers
# def add_numbers(a: int, b: int) -> dict:
#     return {"sum": a + b}

# # ➖ Tool 3: Subtract two numbers
# def subtract_numbers(a: int, b: int) -> dict:
#     return {"difference": a - b}

# # ➗ Tool 4: Divide two numbers
# def divide_numbers(a: int, b: int) -> dict:
#     if b == 0:
#         return {"error": "Division by zero is undefined."}
#     return {"quotient": a / b}

# # 🧠 Wrap custom tools using FunctionTool
# get_current_time_tool = FunctionTool.from_function(
#     func=get_current_time,
#     description="Returns the current time in YYYY-MM-DD HH:MM:SS format",
#     parameters={"type": "object", "properties": {}, "required": []}
# )

# add_numbers_tool = FunctionTool.from_function(
#     func=add_numbers,
#     description="Adds two integers",
#     parameters={
#         "type": "object",
#         "properties": {
#             "a": {"type": "integer"},
#             "b": {"type": "integer"}
#         },
#         "required": ["a", "b"]
#     }
# )

# subtract_numbers_tool = FunctionTool.from_function(
#     func=subtract_numbers,
#     description="Subtracts one integer from another",
#     parameters={
#         "type": "object",
#         "properties": {
#             "a": {"type": "integer"},
#             "b": {"type": "integer"}
#         },
#         "required": ["a", "b"]
#     }
# )

# divide_numbers_tool = FunctionTool.from_function(
#     func=divide_numbers,
#     description="Divides one integer by another",
#     parameters={
#         "type": "object",
#         "properties": {
#             "a": {"type": "integer"},
#             "b": {"type": "integer"}
#         },
#         "required": ["a", "b"]
#     }
# )

# # 🤖 Define the agent
# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Agent with 5 tools: time, add, subtract, divide, and search",
#     instruction="""
#         You are a helpful assistant. You can:
#         - Get the current time
#         - Add, subtract, or divide two numbers
#         - Search the web using google_search
#         Use tools as needed based on user prompts.
#     """,
#     tools=[
#         get_current_time_tool,
#         add_numbers_tool,
#         subtract_numbers_tool,
#         divide_numbers_tool,
#         google_search
#     ]
# )

# # 🧪 Run the agent with a sample prompt
# if __name__ == "__main__":
#     prompt = "What's the current time, and what's 10 divided by 2?"
#     print(root_agent.run(prompt))

# # # 20250826 - Jean Baptiste
# # 2nd attempt to have 5 tools in one agent
# # Microsoft version fixed -

# # Can't ImportError: cannot import name 'Tool' from 'google.adk.tools' (C:\Users\jkamg\OneDrive\Documents\GitHub\agent-development-kit-crash-course\.venv\Lib\site-packages\google\adk\tools\__init__.py)
# # INFO:     127.0.0.1:8464 - "GET /apps/tool_a

# from datetime import datetime
# from google.adk.agents import Agent
# from google.adk.tools import google_search, Tool

# # 🕒 Tool 1: Get current time
# def get_current_time():
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }

# get_current_time_tool = Tool(
#     name="get_current_time",
#     func=get_current_time,
#     description="Returns the current time in YYYY-MM-DD HH:MM:SS format"
# )

# # ➕ Tool 2: Add two numbers
# def add_numbers(a: int, b: int):
#     return {"sum": a + b}

# add_numbers_tool = Tool(
#     name="add_numbers",
#     func=add_numbers,
#     description="Adds two integers",
#     parameters={
#         "type": "object",
#         "properties": {
#             "a": {"type": "integer"},
#             "b": {"type": "integer"}
#         },
#         "required": ["a", "b"]
#     }
# )

# # ➖ Tool 3: Subtract two numbers
# def subtract_numbers(a: int, b: int):
#     return {"difference": a - b}

# subtract_numbers_tool = Tool(
#     name="subtract_numbers",
#     func=subtract_numbers,
#     description="Subtracts one integer from another",
#     parameters={
#         "type": "object",
#         "properties": {
#             "a": {"type": "integer"},
#             "b": {"type": "integer"}
#         },
#         "required": ["a", "b"]
#     }
# )

# # ➗ Tool 4: Divide two numbers
# def divide_numbers(a: int, b: int):
#     if b == 0:
#         return {"error": "Division by zero is undefined."}
#     return {"quotient": a / b}

# divide_numbers_tool = Tool(
#     name="divide_numbers",
#     func=divide_numbers,
#     description="Divides one integer by another",
#     parameters={
#         "type": "object",
#         "properties": {
#             "a": {"type": "integer"},
#             "b": {"type": "integer"}
#         },
#         "required": ["a", "b"]
#     }
# )

# # 🤖 Define the agent
# tool_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Agent with 5 tools: time, add, subtract, divide, and search",
#     instruction="""
#         You are a helpful assistant. You can:
#         - Get the current time
#         - Add, subtract, or divide two numbers
#         - Search the web using google_search
#         Use tools as needed based on user prompts.
#     """,
#     tools=[
#         get_current_time_tool,
#         add_numbers_tool,
#         subtract_numbers_tool,
#         divide_numbers_tool,
#         google_search
#     ]
# )

# # 🧪 Run the agent with a sample prompt
# if __name__ == "__main__":
#     prompt = "What's the current time, and what's 10 divided by 2?"
#     print(tool_agent.run(prompt))

# # still doesn't work -

# # Now claude attempt of multi tools in one agent

# # https://claude.ai/chat/a02c3c6c-ab52-40d8-9dff-43e62badac86


# from google.adk.agents import Agent
# from google.adk.tools import google_search
# from datetime import datetime

# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

# def calculate_numbers(a: int, b: int, operation: str) -> dict:
#     """
#     Perform basic arithmetic operations on two numbers.
    
#     Args:
#         a: The first number
#         b: The second number
#         operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
#     Returns:
#         A dictionary with the calculation result or error message
#     """
#     try:
#         if operation.lower() == 'add':
#             result = a + b
#         elif operation.lower() == 'subtract':
#             result = a - b
#         elif operation.lower() == 'multiply':
#             result = a * b
#         elif operation.lower() == 'divide':
#             if b == 0:
#                 return {"status": "error", "error_message": "Cannot divide by zero"}
#             result = a / b
#         else:
#             return {"status": "error", "error_message": f"Unknown operation: {operation}"}
        
#         return {
#             "status": "success",
#             "result": result,
#             "operation": f"{a} {operation} {b} = {result}"
#         }
#     except Exception as e:
#         return {"status": "error", "error_message": str(e)}

# def get_weather_info(city: str) -> dict:
#     """
#     Get weather information for a specific city (mock data).
    
#     Args:
#         city: The city name to get weather for
        
#     Returns:
#         A dictionary with weather information
#     """
#     # Mock weather data - in reality you'd call a weather API
#     weather_data = {
#         "london": {"temp": "18°C", "condition": "Cloudy", "humidity": "65%"},
#         "paris": {"temp": "22°C", "condition": "Sunny", "humidity": "45%"},
#         "new york": {"temp": "15°C", "condition": "Rainy", "humidity": "70%"},
#         "tokyo": {"temp": "20°C", "condition": "Clear", "humidity": "55%"}
#     }
    
#     city_lower = city.lower()
#     if city_lower in weather_data:
#         data = weather_data[city_lower]
#         return {
#             "status": "success",
#             "city": city.title(),
#             "temperature": data["temp"],
#             "condition": data["condition"],
#             "humidity": data["humidity"]
#         }
#     else:
#         return {
#             "status": "error",
#             "error_message": f"Weather data not available for {city}"
#         }

# # Create the multi-tool agent
# # multi_tool_agent = Agent(

# # tool_agent = Agent(
# #     # name="multi_tool_agent",

# root_agent = Agent(
#     name="tool_agent",
# #     # ... other config
# # )
# #     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="A versatile assistant with multiple capabilities",
#     instruction="""
#     You are a helpful assistant with multiple capabilities:
    
#     1. Time Information: Use 'get_current_time' to get the current date and time
#     2. Calculations: Use 'calculate_numbers' to perform arithmetic (add, subtract, multiply, divide)
#     3. Weather: Use 'get_weather_info' to get weather information for cities
#     4. Web Search: Use 'google_search' to search for current information on the web
    
#     Instructions for tool usage:
#     - Always use the most appropriate tool for the user's request
#     - You can use multiple tools in sequence if needed
#     - For calculations, clearly show the operation and result
#     - For weather, provide a formatted summary
#     - For web search, provide concise and relevant information
#     - If a tool returns an error status, explain the error to the user
    
#     Be conversational and helpful while utilizing these tools effectively.
#     """,
#     tools=[get_current_time, calculate_numbers, get_weather_info, google_search],
# )


# # It seems ams that google searcg if the function   not working
# # Last attempt working of Claude.ai- Jean Baptiste
# # This is working fine - 5 tools in one agent
# # file: tool_agent/agent.py

# # Thank you Claude.ai


# from google.adk.agents import Agent
# from datetime import datetime

# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

# def calculate_numbers(a: int, b: int, operation: str) -> dict:
#     """
#     Perform basic arithmetic operations on two numbers.
    
#     Args:
#         a: The first number
#         b: The second number
#         operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
#     Returns:
#         A dictionary with the calculation result or error message
#     """
#     try:
#         if operation.lower() == 'add':
#             result = a + b
#         elif operation.lower() == 'subtract':
#             result = a - b
#         elif operation.lower() == 'multiply':
#             result = a * b
#         elif operation.lower() == 'divide':
#             if b == 0:
#                 return {"status": "error", "error_message": "Cannot divide by zero"}
#             result = a / b
#         else:
#             return {"status": "error", "error_message": f"Unknown operation: {operation}"}
        
#         return {
#             "status": "success",
#             "result": result,
#             "operation": f"{a} {operation} {b} = {result}"
#         }
#     except Exception as e:
#         return {"status": "error", "error_message": str(e)}

# def get_weather_info(city: str) -> dict:
#     """
#     Get weather information for a specific city (mock data).
    
#     Args:
#         city: The city name to get weather for
        
#     Returns:
#         A dictionary with weather information
#     """
#     # Mock weather data - in reality you'd call a weather API
#     weather_data = {
#         "london": {"temp": "18°C", "condition": "Cloudy", "humidity": "65%"},
#         "paris": {"temp": "22°C", "condition": "Sunny", "humidity": "45%"},
#         "new york": {"temp": "15°C", "condition": "Rainy", "humidity": "70%"},
#         "tokyo": {"temp": "20°C", "condition": "Clear", "humidity": "55%"},
#         "lagos": {"temp": "28°C", "condition": "Partly Cloudy", "humidity": "75%"},
#         "sydney": {"temp": "16°C", "condition": "Windy", "humidity": "60%"}
#     }
    
#     city_lower = city.lower()
#     if city_lower in weather_data:
#         data = weather_data[city_lower]
#         return {
#             "status": "success",
#             "city": city.title(),
#             "temperature": data["temp"],
#             "condition": data["condition"],
#             "humidity": data["humidity"],
#             "summary": f"Weather in {city.title()}: {data['condition']}, {data['temp']}, {data['humidity']} humidity"
#         }
#     else:
#         return {
#             "status": "error",
#             "error_message": f"Weather data not available for {city}. Available cities: London, Paris, New York, Tokyo, Lagos, Sydney"
#         }

# def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> dict:
#     """
#     Convert temperature between Celsius, Fahrenheit, and Kelvin.
    
#     Args:
#         temperature: The temperature value to convert
#         from_unit: The unit to convert from ('C', 'F', 'K')
#         to_unit: The unit to convert to ('C', 'F', 'K')
    
#     Returns:
#         A dictionary with the converted temperature
#     """
#     try:
#         from_unit = from_unit.upper()
#         to_unit = to_unit.upper()
        
#         # Convert to Celsius first
#         if from_unit == 'C':
#             celsius = temperature
#         elif from_unit == 'F':
#             celsius = (temperature - 32) * 5/9
#         elif from_unit == 'K':
#             celsius = temperature - 273.15
#         else:
#             return {"status": "error", "error_message": "Invalid from_unit. Use 'C', 'F', or 'K'"}
        
#         # Convert from Celsius to target unit
#         if to_unit == 'C':
#             result = celsius
#         elif to_unit == 'F':
#             result = celsius * 9/5 + 32
#         elif to_unit == 'K':
#             result = celsius + 273.15
#         else:
#             return {"status": "error", "error_message": "Invalid to_unit. Use 'C', 'F', or 'K'"}
        
#         return {
#             "status": "success",
#             "original": f"{temperature}°{from_unit}",
#             "converted": f"{result:.2f}°{to_unit}",
#             "conversion": f"{temperature}°{from_unit} = {result:.2f}°{to_unit}"
#         }
#     except Exception as e:
#         return {"status": "error", "error_message": str(e)}

# # Create the root agent with multiple custom tools (avoiding google_search to prevent the error)
# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="A versatile assistant with multiple capabilities",
#     instruction="""
#     You are a helpful assistant with multiple capabilities:
    
#     1. **Time Information**: Use 'get_current_time' to get the current date and time
#     2. **Calculations**: Use 'calculate_numbers' to perform arithmetic (add, subtract, multiply, divide)
#     3. **Weather**: Use 'get_weather_info' to get weather information for major cities
#     4. **Temperature Conversion**: Use 'convert_temperature' to convert between Celsius, Fahrenheit, and Kelvin
    
#     **Tool Usage Guidelines:**
#     - Always use the most appropriate tool for the user's request
#     - You can use multiple tools in sequence if needed
#     - For calculations, clearly show the operation and result
#     - For weather, provide a formatted summary
#     - For temperature conversion, show both original and converted values
#     - If a tool returns an error status, explain the error to the user and suggest alternatives
    
#     **Available Cities for Weather:** London, Paris, New York, Tokyo, Lagos, Sydney
    
#     Be conversational and helpful while utilizing these tools effectively. When users ask questions that require multiple steps, break them down and use the appropriate tools in sequence.
#     """,
#     tools=[get_current_time, calculate_numbers, get_weather_info, convert_temperature],
# )


# Another more advanced version with google search working - Jean Baptiste - 20240828
# From claude.ai

# By Jean Baptiste
# Claude.ai version working fine with google search


from google.adk.agents import Agent
from datetime import datetime
import requests
from typing import Dict, Any

def search_web(query: str) -> dict:
    """
    Search the web for information using a custom search implementation.
    
    Args:
        query: The search query string
        
    Returns:
        A dictionary with search results and information
    """
    try:
        # For now, return a structured response that simulates web search
        # In a real implementation, you'd integrate with a search API like Google Custom Search, Bing, or SerpAPI
        
        # Simulate search results based on common queries
        if any(keyword in query.lower() for keyword in ['weather', 'temperature', 'climate']):
            return {
                "status": "success",
                "query": query,
                "results": [
                    {
                        "title": f"Weather information for {query}",
                        "snippet": "Current weather conditions, temperature, and forecast information available through weather services.",
                        "source": "Weather.com"
                    }
                ],
                "summary": f"Search completed for: {query}. Weather-related information found.",
                "note": "This is a simulated search result. In production, integrate with a real search API."
            }
        elif 'distance' in query.lower():
            return {
                "status": "success", 
                "query": query,
                "results": [
                    {
                        "title": f"Distance calculation for {query}",
                        "snippet": "Geographic distance information between cities and locations.",
                        "source": "Maps service"
                    }
                ],
                "summary": f"Search completed for: {query}. Distance information available through mapping services.",
                "note": "This is a simulated search result. In production, integrate with a real search API."
            }
        else:
            return {
                "status": "success",
                "query": query,
                "results": [
                    {
                        "title": f"Search results for: {query}",
                        "snippet": "General information and resources related to your search query.",
                        "source": "Web search"
                    }
                ],
                "summary": f"Search completed for: {query}. Multiple resources found.",
                "note": "This is a simulated search result. To get real web search, integrate with Google Custom Search API, Bing Search API, or SerpAPI."
            }
            
    except Exception as e:
        return {
            "status": "error", 
            "error_message": f"Search failed: {str(e)}",
            "suggestion": "Try a different search query or check your internet connection."
        }


    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def calculate_numbers(a: int, b: int, operation: str) -> dict:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        a: The first number
        b: The second number
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        A dictionary with the calculation result or error message
    """
    try:
        if operation.lower() == 'add':
            result = a + b
        elif operation.lower() == 'subtract':
            result = a - b
        elif operation.lower() == 'multiply':
            result = a * b
        elif operation.lower() == 'divide':
            if b == 0:
                return {"status": "error", "error_message": "Cannot divide by zero"}
            result = a / b
        else:
            return {"status": "error", "error_message": f"Unknown operation: {operation}"}
        
        return {
            "status": "success",
            "result": result,
            "operation": f"{a} {operation} {b} = {result}"
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

def get_weather_info(city: str) -> dict:
    """
    Get weather information for a specific city (mock data).
    
    Args:
        city: The city name to get weather for
        
    Returns:
        A dictionary with weather information
    """
    # Mock weather data - in reality you'd call a weather API
    weather_data = {
        "london": {"temp": "18°C", "condition": "Cloudy", "humidity": "65%"},
        "paris": {"temp": "22°C", "condition": "Sunny", "humidity": "45%"},
        "new york": {"temp": "15°C", "condition": "Rainy", "humidity": "70%"},
        "tokyo": {"temp": "20°C", "condition": "Clear", "humidity": "55%"},
        "lagos": {"temp": "28°C", "condition": "Partly Cloudy", "humidity": "75%"},
        "sydney": {"temp": "16°C", "condition": "Windy", "humidity": "60%"}
    }
    
    city_lower = city.lower()
    if city_lower in weather_data:
        data = weather_data[city_lower]
        return {
            "status": "success",
            "city": city.title(),
            "temperature": data["temp"],
            "condition": data["condition"],
            "humidity": data["humidity"],
            "summary": f"Weather in {city.title()}: {data['condition']}, {data['temp']}, {data['humidity']} humidity"
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather data not available for {city}. Available cities: London, Paris, New York, Tokyo, Lagos, Sydney"
        }

def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> dict:
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.
    
    Args:
        temperature: The temperature value to convert
        from_unit: The unit to convert from ('C', 'F', 'K')
        to_unit: The unit to convert to ('C', 'F', 'K')
    
    Returns:
        A dictionary with the converted temperature
    """
    try:
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        # Convert to Celsius first
        if from_unit == 'C':
            celsius = temperature
        elif from_unit == 'F':
            celsius = (temperature - 32) * 5/9
        elif from_unit == 'K':
            celsius = temperature - 273.15
        else:
            return {"status": "error", "error_message": "Invalid from_unit. Use 'C', 'F', or 'K'"}
        
        # Convert from Celsius to target unit
        if to_unit == 'C':
            result = celsius
        elif to_unit == 'F':
            result = celsius * 9/5 + 32
        elif to_unit == 'K':
            result = celsius + 273.15
        else:
            return {"status": "error", "error_message": "Invalid to_unit. Use 'C', 'F', or 'K'"}
        
        return {
            "status": "success",
            "original": f"{temperature}°{from_unit}",
            "converted": f"{result:.2f}°{to_unit}",
            "conversion": f"{temperature}°{from_unit} = {result:.2f}°{to_unit}"
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

def format_comparison_table(cities_data: str) -> dict:
    """
    Format city comparison data into a structured table format.
    
    Args:
        cities_data: JSON string containing list of city information dictionaries
        
    Returns:
        A dictionary with formatted table data
    """
    try:
        import json
        
        # Parse the JSON string to get the list of cities
        if isinstance(cities_data, str):
            try:
                cities_list = json.loads(cities_data)
            except json.JSONDecodeError:
                return {"status": "error", "error_message": "Invalid JSON format for cities_data"}
        else:
            cities_list = cities_data
            
        if not cities_list:
            return {"status": "error", "error_message": "No city data provided"}
        
        # Create table headers
        headers = ["City", "Country", "Temperature", "Weather", "Distance from Atlanta (km)"]
        
        # Format the data into rows
        table_rows = []
        for city_info in cities_list:
            row = [
                city_info.get("city", "Unknown"),
                city_info.get("country", "Unknown"),
                city_info.get("temperature", "Unknown"),
                city_info.get("weather", "Unknown"),
                city_info.get("distance", "Unknown")
            ]
            table_rows.append(row)
        
        return {
            "status": "success",
            "headers": headers,
            "rows": table_rows,
            "table_summary": f"Comparison table for {len(table_rows)} cities"
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

# Create the root agent with all tools including Google Search
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="A comprehensive assistant with multiple capabilities including web search",
    instruction="""
    You are a helpful assistant with multiple capabilities:
    
    1. **Time Information**: Use 'get_current_time' to get the current date and time
    2. **Calculations**: Use 'calculate_numbers' to perform arithmetic (add, subtract, multiply, divide)
    3. **Weather**: Use 'get_weather_info' to get weather information for major cities (limited data)
    4. **Temperature Conversion**: Use 'convert_temperature' to convert between Celsius, Fahrenheit, and Kelvin
    5. **Web Search**: Use 'search_web' to search for information (currently simulated - shows how to structure real search integration)
    6. **Table Formatting**: Use 'format_comparison_table' to create structured comparison tables
    
    **For Complex City Comparisons (like Atlanta, Buford GA, Paris FR, Stuttgart, Yaounde, Douala):**
    1. Use 'google_search' to find current weather, temperatures, and distances for each city
    2. Search for information about each city individually if needed
    3. Use 'format_comparison_table' to create a structured table
    4. Present findings with detailed descriptions followed by the formatted table
    
    **Search Strategy for City Comparisons:**
    - Search for "current weather temperature [city name]" for each city
    - Search for "distance from Atlanta to [city name]" for distance information
    - Search for "climate weather [city name]" for general weather patterns
    - Combine multiple searches if needed for comprehensive data
    
    **Tool Usage Guidelines:**
    - Always use the most appropriate tool for the user's request
    - For complex comparisons, use multiple google_search calls to gather comprehensive data
    - Use 'format_comparison_table' when presenting city comparison data
    - If a tool returns an error status, explain the error to the user and try alternative searches
    - Present findings with detailed descriptions before showing tables
    
    **Available Cities for Local Weather Tool:** London, Paris, New York, Tokyo, Lagos, Sydney (limited mock data)
    **Use google_search for:** Current weather, specific cities not in local database, distances, and real-time information
    
    Be thorough in your research and present information in a clear, organized manner with both descriptive analysis and structured tables when requested.
    """,
    tools=[get_current_time, calculate_numbers, get_weather_info, convert_temperature, format_comparison_table, search_web],
)
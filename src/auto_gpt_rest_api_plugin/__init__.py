"""This is the REST API plugin for Auto-GPT."""
import os
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate
import requests
import json

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str

def rest_request(method, url, headers=None, body=None):
    """
    Perform a REST request using the provided parameters.

    :param method: HTTP method (GET, POST, PUT, DELETE, PATCH)
    :param url: URL for the request
    :param headers: JSON string of HTTP headers (optional)
    :param json: JSON-serializable object to include in the request body (optional)
    """

    if method not in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
        raise ValueError(f"Invalid HTTP method '{method}'. Allowed methods: GET, POST, PUT, DELETE, PATCH.")

    if headers:
        headers = json.loads(headers)
    if body:
        body = json.loads(body)

    print(f"method={method}")
    print(f"body={body}")
    response = requests.request(method=method, url=url, headers=headers, json=body)
    print(f"SENT")

    # Check the content type of the response
    content_type = response.headers.get('Content-Type', '')

    try:
        if 'application/json' in content_type:
            response_message_body = response.json()
        else:
            response_message_body = response.content.decode('utf-8')
    except Exception as e:
        response_message_body = f"Error while parsing response content: {str(e)}"

    if response.ok:
        return json.dumps({
            "response_status_code": response.status_code,
            "response_message_body": response_message_body,
            "response_headers": dict(response.headers),
        })
    else:
        result = f"The HTTP Request failed with the following HTTP Status Code: {response.status_code}.\n"
        if response_message_body:
            result += f"In addtion, the API returned the following response. Please use this information to debug the issue: {response_message_body}"
        return result


class AutoGPTPluginRestAPI(AutoGPTPluginTemplate):
    """
    This is the Auto-GPT REST API plugin.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-REST-API-Plugin"
        self._version = "0.1.0"
        self._description = "Auto-GPT REST API Plugin: Supercharge REST API management."

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        prompt.add_command(
            "Send REST Request",
            "send_rest_request",
            {
                "method": "<HTTP method>",
                "url": "<url>",
                "headers": "<headers as JSON>",
                "body": "<body as JSON>"
            },
            rest_request
        )
        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.

        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.

        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.

        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.

        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.

        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.

        Args:
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.

        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.

        Args:
            messages (List[Message]): The list of context messages.

        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.

        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.

        Args:
            messages (List[Message]): The list of context messages.

        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.

        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.

        Args:
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.

        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.

        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.

        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.

        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.

        Args:
            command_name (str): The command name.
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.

        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.

          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.

        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.

        Returns:
            str: The resulting response.
        """
        pass

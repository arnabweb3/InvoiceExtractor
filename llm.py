from abc import ABC, abstractmethod
from google import genai
from google.genai.types import GenerateContentConfig


class LLM:

    # @abstractmethod
    # def __init__(self):
    #     pass

    @abstractmethod
    def generate_response(self,prompt) -> str:
        pass


class Gemini():
    def __init__(self):
        self.client = genai.Client()

    def generate_response(self,prompt) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config=GenerateContentConfig(
                temperature=0,
            )
        )

        assert response.text is not None
        return response.text 


     

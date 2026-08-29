from typing import TypeVar

T = TypeVar("T", bound=AIModel)

class AIModel:
    def generate(self):
        pass


class GPTModel(AIModel):
    pass


class GeminiModel(AIModel):
    pass    



def load_model(model: T) -> T:
    return model


gemini=GeminiModel()
print(load_model(gemini))
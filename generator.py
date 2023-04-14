from transformers import pipeline


generator = pipeline("text-generation", "gpt2")


class Generator:
    def __init__(self):
        self.generator = generator

    def generate_text(self, text: str, text_len: int):
        """Text generation using user input
        - **text**: input user text
        - **text_len**: count of output symbols
        """
        if text_len <= 0:
            message = "Length is not valid. "\
                      "Length should be more than 0."
            return {"Message": message}
        try:
            result_text = self.generator(text, max_length=text_len)
        except Exception as e:
            message = f"Parameters are not valid. {e}."\
                    f"I don't know what to say"
            return {"Message": message}
        return {"generated_text": result_text[0]['generated_text']}

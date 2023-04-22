from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from styleformer import Adequacy

tokenizer = AutoTokenizer.from_pretrained("prithivida/informal_to_formal_styletransfer")
model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/informal_to_formal_styletransfer")
adequacy = "prithivida/parrot_adequacy_model" and Adequacy(model_tag="prithivida/parrot_adequacy_model")


class Generator:
    def __init__(self):
        self.tokenizer = tokenizer
        self.model = model
        self.adequacy = adequacy

    def _casual_to_formal(self, input_sentence):
        input_ids = self.tokenizer.encode(input_sentence, return_tensors='pt')

        preds = self.model.generate(
            input_ids,
            do_sample=True,
            max_length=32,
            top_k=50,
            top_p=0.95,
            early_stopping=True,
            num_return_sequences=5)

        gen_sentences = set()
        for pred in preds:
            gen_sentences.add(self.tokenizer.decode(pred, skip_special_tokens=True).strip())

        adequacy_scored_phrases = self.adequacy.score(input_sentence, list(gen_sentences), 0.95)
        ranked_sentences = sorted(adequacy_scored_phrases.items(), key=lambda x: x[1], reverse=True)
        if len(ranked_sentences) > 0:
            return ranked_sentences[0][0]
        else:
            return None

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
            result_text_list = []
            sentences = text.split(".")
            for sentence in sentences:
                if len(sentence) > 0:
                    formal_text = self._casual_to_formal(sentence)
                    if formal_text is not None:
                        result_text_list.append("".join([formal_text, " "]))
        except Exception as e:
            message = f"Parameters are not valid. {e}."\
                    f"I don't know what to say"
            return {"Message": message}
        return {"generated_text": "".join(result_text_list)}

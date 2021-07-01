import torch
from transformers import AutoTokenizer, AutoModel
import numpy
from utils import get_data_model_path


class Embedder:
    def __init__(self) -> None:
        self.load_model()

    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny", cache_dir = get_data_model_path())
        self.model = AutoModel.from_pretrained("cointegrated/rubert-tiny", cache_dir = get_data_model_path())

    def compute_embeddings(self, phrases: list) -> numpy.ndarray:
        t = self.tokenizer(phrases, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = self.model(
                **{k: v.to(self.model.device) for k, v in t.items()}
            )
        embeddings = model_output.last_hidden_state[:, 0, :]
        embeddings = torch.nn.functional.normalize(embeddings)
        embeddings = embeddings.cpu().numpy()
        return embeddings


if __name__ == "__main__":
    print(get_data_model_path())
    exp = Embedder()
    text = [
        "погода в москве",  
        "погода в питере",
        "расскажи мне какая сейчас погода в новосибирске",
    ]    
    print(exp.compute_embeddings(text))
'''
расстояние между "погода в москве" и "погода в питере" 0.03233879804611206
расстояние между "погода в москве" и "расскажи мне какая сейчас погода в новосибирске" 0.41958218812942505

'''

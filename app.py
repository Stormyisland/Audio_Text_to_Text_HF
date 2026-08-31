from transformers import VoxtralForConditionalGeneration, AutoProsessor

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pre_trained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(


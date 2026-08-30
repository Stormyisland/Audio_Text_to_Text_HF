from transformers import VoxtralForConditionalGeneration, AutoProsessor

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.form_pre_trained(repo_id)

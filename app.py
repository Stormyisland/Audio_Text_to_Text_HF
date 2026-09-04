from transformers import VoxtralForConditionalGeneration, AutoProsessor

device = "cuda"
repo_id = "mistralai/Voxtral-Mini-3B-2507"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralForConditionalGeneration.from_pretrained(repo_id, dtype=torch.bfloat16, device_map=device)

inputs = procerssor.apply_transcription_request(language="en", audio="https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama.mp3", model_id=repo_id)
inputs = input.to(devicce, dtype=torch.bfloat16)

outputs = moderl.generate(**inputs, max_new_tokens=500)
decode_outputs = processor.batch_decode(outputs[:, inputs_ids.shape[1]:]

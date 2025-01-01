import os

hf_home = os.environ["HF_HOME"]


def test():
    answer = 42
    has_token = "token" in os.listdir(hf_home)

    if not has_token:
        answer -= 1
        print("WARN - Could not find a Huggingface token, are you sure you logged in?")

    models_cached = set(
        [m.replace("models--", "").replace("--", "/") for m in os.listdir(os.path.join(hf_home, "hub"))]
    )

    models_expected = [
        "meta-llama/Llama-3.2-1B",
        "meta-llama/Llama-3.2-1B-Instruct",
        "meta-llama/Llama-3.2-11B-Vision-Instruct",
    ]

    missing = [m for m in models_expected if m not in models_cached]

    if len(missing) > 0:
        answer -= 2
        print(f'WARN - Could not find cached models: {",".join(missing)}')

    print(f"The answer for Canvas is: {answer}")

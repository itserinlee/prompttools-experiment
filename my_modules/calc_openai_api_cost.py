import tiktoken


def countTokens(text: str, modelName: str) -> int:
    encoding = tiktoken.encoding_for_model(modelName)
    return len(encoding.encode(text)) # number of tokens


def calcAPICost(
    outputTokenLimit: int,
    models: list[str],
    prompts: list[str]
    ):

    ## cost per 1K output tokens for each model
    cost_per_1k_tokens = {
        "gpt-4": 0.06,
        "gpt-3.5-turbo": 0.0015
    }

    ## calculate total tokens and cost for each model
    total_cost = {}
    for model in models:
        total_tokens = sum(countTokens(msg, model) for msg in prompts) + outputTokenLimit * len(prompts)
        total_cost[model] = (total_tokens / 1000) * cost_per_1k_tokens[model]
    print(f'{total_cost=}')



if __name__ == '__main__':

    models = ["gpt-3.5-turbo", "gpt-4"]
    prompts = [
        "Tell me a joke.",
        "Is 17077 a prime number?"
    ]
    outputTokenLimit=[60]

    calcAPICost(
        outputTokenLimit,
        models,
        prompts
    )
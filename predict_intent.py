from transformers import BertForSequenceClassification, BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

model = BertForSequenceClassification.from_pretrained(
    "models/my_trained_model_get_weather"
)


def predict_intent(message):
    inputs = tokenizer(message, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=-1).item()
    return predictions


def get_intent_name(user_message):
    intent = predict_intent(user_message)

    intent_mapping = {0: "weather", 1: "joke", 2: "greeting"}
    return intent_mapping[intent]

"""
Training Script for Yoruba Constituency Parsing
Author: Victoria Akindele
Project: Yoruba Constituency Treebank (Version 1.0)

This script fine-tunes a transformer-based sequence-to-sequence model
to learn Yoruba constituency structures from manually annotated data.
"""

import pandas as pd
from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Trainer,
    TrainingArguments
)
from torch.utils.data import Dataset


# -----------------------------
# Custom Dataset Class
# -----------------------------
class YorubaTreebankDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_length=256):
        self.data = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sentence = self.data.iloc[idx]["sentence"]
        tree = self.data.iloc[idx]["Phrase Structure"]

        input_text = f"parse: {sentence}"
        target_text = tree

        inputs = self.tokenizer(
            input_text,
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )

        targets = self.tokenizer(
            target_text,
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )

        return {
            "input_ids": inputs["input_ids"].squeeze(),
            "attention_mask": inputs["attention_mask"].squeeze(),
            "labels": targets["input_ids"].squeeze()
        }


# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Yoruba Treebank...")
df = pd.read_csv("yoruba_treebank.csv")

# Keep only required columns
df = df[["sentence", "Phrase Structure"]]
df = df.dropna()

# -----------------------------
# Load Model & Tokenizer
# -----------------------------
print("Loading tokenizer and model...")
model_name = "t5-small"  # lightweight and suitable for experiments
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# -----------------------------
# Prepare Dataset
# -----------------------------
dataset = YorubaTreebankDataset(df, tokenizer)

# -----------------------------
# Training Configuration
# -----------------------------
training_args = TrainingArguments(
    output_dir="./yoruba_parser_model",
    evaluation_strategy="no",
    learning_rate=5e-5,
    per_device_train_batch_size=4,
    num_train_epochs=5,
    weight_decay=0.01,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=50,
    save_strategy="epoch",
    report_to="none"
)

# -----------------------------
# Trainer
# -----------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer
)

# -----------------------------
# Train Model
# -----------------------------
print("Starting training...")
trainer.train()

# -----------------------------
# Save Model
# -----------------------------
print("Saving model...")
trainer.save_model("./yoruba_parser_model")
tokenizer.save_pretrained("./yoruba_parser_model")

print("Training completed successfully.")

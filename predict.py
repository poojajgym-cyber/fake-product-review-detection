import pickle

# Load model + vectorizer
with open("model/fake_review_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

print("🔮 Fake Review Detector (type 'exit' to quit)\n")

while True:
    review = input("Enter a review: ")
    if review.lower() == "exit":
        break
    
    X_new = vectorizer.transform([review])
    prediction = model.predict(X_new)[0]

    if prediction == 1:
        print("✅ Genuine Review\n")
    else:
        print("❌ Fake Review\n")

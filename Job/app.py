

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Define the interests array
l1 = ['Database Fundamentals', 'Computer Architecture', 'Distributed Computing Systems', 'Cyber Security', 'Networking', 'Software Development', 'Programming Skills', 'Project Management', 'Computer Forensics Fundamentals', 'Technical Communication', 'AI ML', 'Software Engineering', 'Business Analysis', 'Communication skills', 'Data Science', 'Troubleshooting skills', 'Graphics Designing']

# Load the pickled decision tree model
with open('random_forest_model (2).pkl', 'rb') as f:
    model = pickle.load(f)

# Define routes
@app.route('/')
def index():
    return render_template('index.html', interests=l1)

# Define the course options
Role = ['AI ML Specialist',
          'API Integration Specialist',
          'Application Support Engineer',
          'Business Analyst',
          'Customer Service Executive',
          'Cyber Security Specialist',
          'Data Scientist',
          'Database Administrator',
          'Graphics Designer',
          'Hardware Engineer',
          'Helpdesk Engineer',
          'Information Security Specialist',
          'Networking Engineer',
          'Project Manager',
          'Software Developer',
          'Software Tester',
          'Technical Writer']

@app.route('/predict', methods=['POST'])
def predict():
    selected_interests = request.form.getlist('interests')
    
    # Convert selected interests to one-hot encoding
    selected_interests_encoded = [1 if interest in selected_interests else 0 for interest in l1]
    
    # Reshape the encoded interests to a 2D array
    selected_interests_encoded = [selected_interests_encoded]

    # Use the decision tree model to predict
    predicted_course_index = model.predict(selected_interests_encoded)[0]
    
    predicted_course = Role[predicted_course_index]

    return render_template('result.html', predicted_course=predicted_course)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

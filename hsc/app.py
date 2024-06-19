from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# List of interests
interests = [
    'Drawing', 'Dancing', 'Singing', 'Sports', 'Video Game', 'Acting', 'Travelling', 'Gardening', 'Animals',
    'Photography', 'Teaching', 'Exercise', 'Coding', 'Electricity Components', 'Mechanic Parts', 'Computer Parts',
    'Researching', 'Architecture', 'Historic Collection', 'Botany', 'Zoology', 'Physics', 'Accounting', 'Economics',
    'Sociology', 'Geography', 'Psychology', 'History', 'Science', 'Business Education', 'Chemistry', 'Mathematics',
    'Biology', 'Makeup', 'Designing', 'Content writing', 'Crafting', 'Literature', 'Reading', 'Cartooning',
    'Debating', 'Astrology', 'Hindi', 'French', 'English', 'Other Language', 'Solving Puzzles', 'Gymnastics',
    'Yoga', 'Engineering', 'Doctor', 'Pharmacist', 'Cycling', 'Knitting', 'Director', 'Journalism', 'Business',
    'Listening Music','Communication'
]

# Load the trained model
with open('course_prediction_model (1).pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html', interests=interests)

course_labels = [
        'BBA- Bachelor of Business Administration', 'BEM- Bachelor of Event Management',
        'Integrated Law Course- BA + LL.B', 'BJMC- Bachelor of Journalism and Mass Communication',
        'BFD- Bachelor of Fashion Designing', 'BBS- Bachelor of Business Studies',
        'BTTM- Bachelor of Travel and Tourism Management', 'BVA- Bachelor of Visual Arts',
        'BA in History', 'B.Arch- Bachelor of Architecture', 'BCA- Bachelor of Computer Applications',
        'B.Sc.- Information Technology', 'B.Sc- Nursing', 'BPharma- Bachelor of Pharmacy',
        'BDS- Bachelor of Dental Surgery', 'Animation, Graphics and Multimedia',
        'B.Sc- Applied Geology', 'B.Sc.- Physics', 'B.Sc. Chemistry', 'B.Sc. Mathematics',
        'B.Tech.-Civil Engineering', 'B.Tech.-Computer Science and Engineering',
        'B.Tech.-Electrical and Electronics Engineering', 'B.Tech.-Electronics and Communication Engineering',
        'B.Tech.-Mechanical Engineering', 'B.Com- Bachelor of Commerce', 'BA in Economics',
        'CA- Chartered Accountancy', 'CS- Company Secretary', 'Diploma in Dramatic Arts',
        'MBBS', 'Civil Services', 'BA in English', 'BA in Hindi', 'B.Ed.'
    ]
@app.route('/predict', methods=['POST'])
def predict():
    selected_interests = request.form.getlist('interests')
    
    # Convert selected interests to one-hot encoding
    selected_interests_encoded = [1 if interest in selected_interests else 0 for interest in interests]
    
    # Use the model to predict
    predicted_course_name = model.predict([selected_interests_encoded])[0]  # Get the predicted course name directly

# Find the index of the predicted course name in the list of course labels
    predicted_course_index = course_labels.index(predicted_course_name)
    
    
    predicted_course = course_labels[predicted_course_index]  # Access course label using the integer index
    
    return render_template('result.html', predicted_course=predicted_course)


if __name__ == '__main__':
    app.run(debug=True,port=5001)

# Video Anomaly Detection System

# Overview
The Video Anomaly Detection System is a sophisticated web-based application designed to identify and report anomalies in video footage. Leveraging advanced machine learning algorithms, this system can automatically flag unusual patterns or events without human intervention. The application is built on Flask, a lightweight Python web framework, ensuring quick deployment and ease of use.

# Features
1) User-Friendly Interface: The application boasts a Netflix-like dark theme, making the navigation and interaction intuitive and visually appealing.
2) Live Animated Background: The dynamic gradient background creates a lively and engaging user experience, resonating with the modern web design trends.
3) File Upload Capability: Users can easily upload video files directly through the web interface. The system accepts a range of video formats for analysis.
4) Black & White Themed Buttons: With an aesthetic reminiscent of classic cinema, the interactive buttons on the site feature a cool hover animation effect, enhancing the user experience.
5) Real-Time Processing: Once a video is uploaded, the system promptly processes the footage frame by frame to detect any anomalies.
6) Anomaly Highlighting: Detected anomalies are highlighted, and details are provided to the user for further action.

# Technologies Used
*Flask:* A micro web framework for Python, used to create the web application's backend.\t
*OpenCV:* An open-source computer vision and machine learning software library used for the video processing tasks.\t
*CSS Animations:* Pure CSS is used to create subtle animations and transitions for a more dynamic UI without impacting performance.\t
*HTML5:* Structuring the web application’s content with the latest standards of HTML.\t

# How to Use
*Access the Web Application:* Navigate to the deployed web application URL on any modern web browser.
*Upload Video:* Use the central upload button to select and upload a video file from your local system.
*Anomaly Detection:* The system processes the uploaded video and displays the results, highlighting any detected anomalies.

# Potential Use Cases
1) Security Monitoring: Ideal for surveillance video analysis in public areas, private properties, or restricted zones.
2) Quality Control: In manufacturing or production lines to detect deviations from standard procedures.
3) Traffic Regulation: Monitoring traffic flow and detecting unusual behavior like wrong-way driving or accidents.

# Getting Started
To set up the project locally, follow these steps:

Clone the repository to your local machine.
Install the required dependencies via *pip install -r requirements.txt.*
Run the Flask application using flask run or python *application.py.*

# Future Enhancements
-Integration of AI models for improved anomaly detection accuracy.
-Real-time video streaming capability for live surveillance footage analysis.
-User authentication system to secure access to the video analysis results.
-Scalability improvements to handle simultaneous video processing from multiple users.

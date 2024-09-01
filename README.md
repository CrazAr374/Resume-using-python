# Resume Maker in Python

A simple Python script to create a formatted resume by taking user input for various sections like personal details, education, work experience, and skills. The output is displayed in a neatly formatted table using the `tabulate` library.

## Features

- **Interactive Input**: The script interactively prompts the user to enter their personal information, education details, work experience, and skills.
- **Formatted Output**: Displays the resume data in a structured table format for easy reading.
- **Easy to Use**: Just run the script and follow the prompts.

## Requirements

- Python 3.x
- `tabulate` library

You can install the `tabulate` library using pip:

```bash
pip install tabulate
```

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/resume-maker.git
   cd resume-maker
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, and then install the `tabulate` library if you haven't already:

   ```bash
   pip install tabulate
   ```

3. **Run the Script**:
   Execute the Python script to start creating your resume:

   ```bash
   python resume_maker.py
   ```

4. **Enter Your Information**:
   Follow the prompts to input your:
   - Name
   - Email
   - Phone number
   - Address
   - Education details (multiple entries allowed)
   - Work experience (multiple entries allowed)
   - Skills (comma-separated list)

5. **View Your Resume**:
   The script will display your resume in a formatted table in the console.

## Example Output

```
Resume
========================================
Basic Information:
+----------------+--------------------+-------------+------------------+
| Name           | Email              | Phone       | Address          |
+================+====================+=============+==================+
| John Doe       | john@example.com   | 123-456-7890| 123 Main St      |
+----------------+--------------------+-------------+------------------+

Education:
+------------------+------------------------+------+
| Degree           | Institution            | Year |
+==================+========================+======+
| B.Sc. Computer Science | University XYZ   | 2022 |
+------------------+------------------------+------+

Work Experience:
+-----------------+----------------+------------+
| Job Title       | Company        | Years      |
+=================+================+============+
| Software Engineer | ABC Corp     | 2022-2024  |
+-----------------+----------------+------------+

Skills:
- Python
- Java
- Web Development
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to improve this script.

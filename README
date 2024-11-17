**QuickJSONtoCSV**

QuickJSONtoCSV is a powerful and simple tool for converting JSON files to CSV format. This project offers a lightweight and scalable RESTful API for conversion and includes advanced features such as automatic handling of nested JSON. Designed with the KISS (Keep It Simple, Stupid) principle, it ensures intuitive implementation and high performance for a variety of use cases.

**Key Features**
- **RESTful API for Conversion**: Easily send JSON files and receive the converted CSV file.
- **Support for Nested JSON**: Complex JSON structures are automatically flattened, allowing for direct and accurate conversion.
- **Compatibility with Large Files**: Efficient conversion of large JSON datasets using streaming to avoid memory overload.
- **JSON Validation**: Ensures the quality and validity of the input JSON file.
- **Caching Results**: Improves performance for repeated conversions.

**Requirements**
- Python 3.7 or higher
- FastAPI and Uvicorn for the RESTful API
- pandas for data handling

**Installation**
Clone the repository:
```bash
git clone https://github.com/yourusername/QuickJSONtoCSV.git
cd QuickJSONtoCSV
```
Create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
Install dependencies:
```bash
pip install -r requirements.txt
```

**Usage**
Start the API server:
```bash
uvicorn backend.api:app --reload
```
The API will be available at [http://localhost:8000/convert/](http://localhost:8000/convert/).

**API Endpoint**
- **POST /convert/**: Send a JSON file for conversion to CSV.

Example usage with curl:
```bash
curl -X 'POST' \
  'http://localhost:8000/convert/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@backend/simple_test.json'
```

**Automated Tests**
Run automated tests using pytest to verify backend functionality:
```bash
pytest backend/test_api.py
```

**Project Structure**
- `backend/`
  - `api.py`: Contains the FastAPI-based RESTful API.
  - `converter.py`: Functions for converting JSON to CSV, including nested data handling and streaming.
  - `simple_test.json`: Example test file with simple data.
  - `nested_test.json`: Example test file with nested JSON data.
  - `requirements.txt`: Project dependencies list.

**Advanced Features**
- **Automatic Handling of Nested JSON**: The project supports automatic conversion of nested JSON structures into a flattened CSV format, simplifying data analysis.
- **Streaming for Large Files**: Data conversion uses efficient streaming to handle large files, avoiding memory overload.
- **JSON Security and Validation**: Input JSON files are validated to ensure reliable and secure conversion.

**Contributions**
Contributions and suggestions are welcome! Feel free to open issues or pull requests.

**License**
This project is released under the MIT license.
import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

from classify import classify

app = FastAPI()

@app.post("/classify/")
async def classify_logs(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(file.file)
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV file must contain 'source' and 'log_message' columns.")

        # Perform classification
        df['Target_label'] = classify(list(zip(df['source'], df['log_message'])))
        print("Dataframe:", df.to_dict())
    
        
        # Save the classified results to a new CSV file
        output_file_path = 'Resources/output.csv'
        df.to_csv(output_file_path, index=False)
        print("File saved to:", output_file_path)
        return FileResponse(output_file_path, media_type='text/csv')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during processing: {str(e)}")
    finally:
        file.file.close()  # Close the file to free up resources
    # Return the classified CSV file
    
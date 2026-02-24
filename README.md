# Music Streaming Analysis Using Spark Structured APIs

## Overview

## Dataset Description

## Repository Structure

## Output Directory Structure

## Tasks and Outputs

## Execution Instructions

## _Prerequisites_

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. _Python 3.x_:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. _PySpark_:
   - Install using pip:
     ```bash
     pip install pyspark
     ```

3. _Apache Spark_:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

### _2. Running the Analysis Tasks_

#### _Running Locally_

1. _Generate the Input_:

```bash
 python3 input_generator.py
```

2. **Execute Each Task Using spark-submit**:

   ```bash
     spark-submit main.py
   ```

3. _Verify the Outputs_:
   Check the outputs/ directory for the resulting files:
   ```bash
   ls outputs/
   ```

## Errors and Resolutions

- I was unable to run the `pip install pyspark` command. So, I reinstalled the latest version of Python, forced it to incluce `pip` and edited my System Environment Variables to force `Command Prompt` to use that installation.
- When installing Apache Spark, I had errors running `spark-submit main.py`, saying the command was not found. I found that I had to include the installation directory as environment variable: `%SPARK_HOME%`, and then add `%SPARK_HOME/bin` as a path.
- `python3 input_generator.py` lists the wrong file name. It should be `datagen.py`
- Running gave me a large error log. So I had to install Hadoop, and set it up similarly to Apache Spark.

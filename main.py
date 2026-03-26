import logging

logging.basicConfig(filename="audit.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")

def process_data(file_path):
    success=0
    error=0
    t_revenue=0

    print(f"=====Starting Audit For :{file_path} =====")
    logging.info(f"===New Audit For:{file_path} ===")

    try:
        with open(file_path,"r") as file:
            header=next(file)
            header_data=header.strip().split(",")
            colum=len(header_data)

            print(f"Expected Colum In This File:{colum}")
            logging.info(f"Expected Colum:{colum}")

            for line_no,line in enumerate(file,start=2):
                data_0=line.strip()
                data=data_0.split(",")

                if len(data) != colum:
                    error=error+1
                    continue
                    logging.warning(f"Line:{line_no} Colum Mismatch Expected:{colum} but found:{len(data)}")

                try:
                    ammount=float(data[2])
                    if ammount <= 0:
                        raise ValueError(f"Invalid transaction amount: {ammount}")

                    t_revenue=t_revenue+ammount
                    success=success+1

                except (ValueError, IndexError) as e:
                    logging.error(f"Line {line_no} [ID: {data[0]}]: Validation failed -> {e}")
                    error=error+1
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
    except Exception as e:
        print("A major error occurred. Please check the logs.")
        logging.critical(f"⚠️ Critical System Failure: {e}")


    print("-------Audit Sumary-------")
    print(f"Target File: {file_path}")
    print(f"Columns: {colum}")
    print(f"Successful Rows: {success}")
    print(f"Failed/Skipped Rows: {error}")
    print(f"Total Value: ${t_revenue:,.2f}")
    print("Detailed audit results are saved in 'audit.log'")

if __name__ == "__main__":
    target_file = "company_big_data.csv" 
    process_data(target_file)

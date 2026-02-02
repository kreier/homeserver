import os
import pandas as pd

def get_folder_info(root_folder):
    folder_data = []

    for dirpath, dirnames, filenames in os.walk(root_folder):
        folder_size = 0
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                folder_size += os.path.getsize(fp)

        folder_data.append({
            "Folder": dirpath,
            "Subfolders": len(dirnames),
            "Files": len(filenames),
            "Size (Bytes)": folder_size
        })

    return folder_data

def export_results(folder_data, csv_file, excel_file):
    df = pd.DataFrame(folder_data)
    df.to_csv(csv_file, index=False)
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    root_folder = "/srv/wordpress"
    csv_file = "size_wordpress.csv"
    excel_file = "size_wordpress.xlsx"

    folder_data = get_folder_info(root_folder)
    export_results(folder_data, csv_file, excel_file)

    print(f"Export completed: {csv_file}, {excel_file}")

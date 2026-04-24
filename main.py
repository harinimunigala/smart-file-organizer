import os
import shutil
from pathlib import Path

# Dictionary mapping file extensions to categories
FILE_CATEGORIES = {
    # Images
    'jpg': 'Images', 'jpeg': 'Images', 'png': 'Images', 'gif': 'Images',
    'bmp': 'Images', 'svg': 'Images', 'webp': 'Images', 'ico': 'Images',
    
    # Documents
    'pdf': 'Documents', 'doc': 'Documents', 'docx': 'Documents',
    'txt': 'Documents', 'xls': 'Documents', 'xlsx': 'Documents',
    'ppt': 'Documents', 'pptx': 'Documents', 'csv': 'Documents',
    
    # Videos
    'mp4': 'Videos', 'mkv': 'Videos', 'avi': 'Videos', 'mov': 'Videos',
    'flv': 'Videos', 'wmv': 'Videos', 'webm': 'Videos', 'mov': 'Videos',
    
    # Audio
    'mp3': 'Audio', 'wav': 'Audio', 'flac': 'Audio', 'aac': 'Audio',
    'm4a': 'Audio', 'ogg': 'Audio', 'wma': 'Audio', 'alac': 'Audio',
    
    # Code
    'py': 'Code', 'js': 'Code', 'html': 'Code', 'css': 'Code',
    'java': 'Code', 'cpp': 'Code', 'c': 'Code', 'rb': 'Code',
    'go': 'Code', 'rs': 'Code', 'php': 'Code', 'sql': 'Code',
    
    # Archives
    'zip': 'Archives', 'rar': 'Archives', '7z': 'Archives',
    'tar': 'Archives', 'gz': 'Archives', 'iso': 'Archives',
}


def get_category(file_extension):
    """
    Get the category folder for a file extension.
    
    Args:
        file_extension (str): The file extension (without the dot)
    
    Returns:
        str: Category name, or 'Other' if not found
    """
    return FILE_CATEGORIES.get(file_extension.lower(), 'Other')


def organize_files(folder_path):
    """
    Organize all files in a folder into category subfolders.
    
    Args:
        folder_path (str): Path to the folder to organize
    
    Returns:
        dict: Summary with counts of organized files
    """
    try:
        # Convert to Path object for cross-platform compatibility
        folder = Path(folder_path)
        
        # Validate folder exists
        if not folder.exists():
            print(f"❌ Error: Folder '{folder_path}' does not exist!")
            return None
        
        if not folder.is_dir():
            print(f"❌ Error: '{folder_path}' is not a folder!")
            return None
        
        # Get all files in the folder (non-recursive)
        files = [f for f in folder.iterdir() if f.is_file()]
        
        if not files:
            print(f"ℹ️  No files found in '{folder_path}'")
            return {'total': 0, 'organized': 0, 'failed': 0}
        
        organized_count = 0
        failed_count = 0
        summary = {}
        
        print(f"\n🚀 Starting to organize {len(files)} files...\n")
        
        for file in files:
            # Skip hidden files (starting with .)
            if file.name.startswith('.'):
                continue
            
            # Get file extension
            file_extension = file.suffix[1:]  # Remove the dot
            
            # Determine category
            category = get_category(file_extension)
            
            # Create category folder if it doesn't exist
            category_folder = folder / category
            category_folder.mkdir(exist_ok=True)
            
            # Determine destination path
            destination = category_folder / file.name
            
            # Handle duplicate filenames
            if destination.exists():
                # Add number to filename (e.g., photo(1).jpg)
                name, ext = file.name.rsplit('.', 1) if '.' in file.name else (file.name, '')
                counter = 1
                while destination.exists():
                    new_name = f"{name}({counter}).{ext}" if ext else f"{name}({counter})"
                    destination = category_folder / new_name
                    counter += 1
            
            try:
                # Move file to category folder
                shutil.move(str(file), str(destination))
                organized_count += 1
                
                # Track summary
                summary[category] = summary.get(category, 0) + 1
                
                print(f"✅ Moved: {file.name} → {category}/")
            
            except Exception as e:
                failed_count += 1
                print(f"❌ Failed to move {file.name}: {str(e)}")
        
        # Print summary
        print(f"\n{'='*50}")
        print(f"✨ Organization Complete!")
        print(f"{'='*50}")
        print(f"📊 Total files organized: {organized_count}")
        print(f"❌ Failed: {failed_count}")
        print(f"\n📂 Breakdown:")
        for category, count in sorted(summary.items()):
            print(f"   {category}: {count} files")
        print(f"{'='*50}\n")
        
        return {'total': len(files), 'organized': organized_count, 'failed': failed_count}
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def main():
    """Main function to run the file organizer."""
    print("\n" + "="*50)
    print("🗂️  SMART FILE ORGANIZER")
    print("="*50)
    print("Organize your messy folders automatically!\n")
    
    # Get folder path from user
    folder_path = input("📁 Enter the folder path to organize: ").strip()
    
    # Remove quotes if user accidentally added them
    folder_path = folder_path.strip('"\'')
    
    # Organize files
    result = organize_files(folder_path)
    
    if result is None:
        print("Please check the folder path and try again.")
    elif result['organized'] == 0 and result['total'] == 0:
        print("No files to organize.")
    else:
        print("🎉 Your folder is now organized!")


if __name__ == "__main__":
    main()

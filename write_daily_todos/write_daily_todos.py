def write_daily_todos(
    self,
    must: Optional[list[str]] = None,
    should: Optional[list[str]] = None,
    want: Optional[list[str]] = None
) -> str:
    """
    Adds today's todos to the Tasks section of Obsidian daily note.

    This function takes in three different lists of todos organized into must, should, 
    and want categories and writes them to the Obsidian daily note in their respective category.

    Args:
        must (Optional[list[str]]): Today's tasks that are in the must category.
                              If not provided, defaults to none.
        should (Optional[list[str]]): Today's tasks that are in the should category.
                              If not provided, defaults to none.
        want (Optional[list[str]]): Today's tasks that are in the want category.
                              If not provided, defaults to none.

    Returns:
        str: Whether or not the operation succeeded, or an error message if one occurs.
    
    Raises:
        FileNotFoundError: If the daily note file does not exist.

    Example:
        >>> write_daily_todos(["do something important"], ["work on something"], ["leisure time"])
        "Successfully added todos to daily note.
    """
    import datetime
    import os
    import re

    # Fetch current daily note.
    date = datetime.date.today().isoformat()
    VAULT_FOLDER = "<folder here>"
    daily_note_path = os.path.join(VAULT_FOLDER, f"{date}.md")

    # Read the daily note
    try:
        with open(daily_note_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        return f"Error: Daily note for {date} not found."
    
    tasks_pattern = r'## ✅ Tasks\n(.*?)(?=\n##|\Z)' # NOTE: This is where I put tasks. This is likely different to you.
    tasks_match = re.search(tasks_pattern, content, re.DOTALL)

    if tasks_match:
        tasks_section = tasks_match.group(1)
        new_tasks_section = "## ✅ Tasks\n"
        new_tasks_section += "### **Must, Should, Want**\n"

        # Function to format tasks
        def format_tasks(category, tasks):
            if tasks:
                due_date = f"📅 {date}"
                formatted = f"#### ***{category}***\n"
                for task in tasks:
                    formatted += f"- [ ] {task} {due_date}\n"
                return formatted
            return ""

        # Add tasks to their respective section.
        new_tasks_section += format_tasks("Must", must)
        new_tasks_section += format_tasks("Should", should)
        new_tasks_section += format_tasks("Want", want)

        # Replace old tasks section with new one
        updated_content = content.replace(tasks_match.group(0), new_tasks_section)

        # Write updated content back to file
        with open(daily_note_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        return "Successfully added todos to daily note."
    else:
        return "Error: Tasks section not found in the daily note."
ax.query = f"""
    SELECT <ax_fields> 
    FROM "<ax_table>"
    WHERE "author"="{ax.user_email}";
"""

import os

def clean_po(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('\n\n')
    new_blocks = []
    seen_msgids = set()
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        lines = block.split('\n')
        msgid_line = None
        for line in lines:
            if line.startswith('msgid '):
                msgid_line = line
                break
        
        if msgid_line:
            # Always keep the header (msgid "")
            if msgid_line == 'msgid ""' or msgid_line not in seen_msgids:
                seen_msgids.add(msgid_line)
                new_blocks.append(block)
            else:
                print(f"Removing duplicate: {msgid_line}")
        else:
            new_blocks.append(block)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(new_blocks))

if __name__ == "__main__":
    clean_po('locale/rw/LC_MESSAGES/django.po')

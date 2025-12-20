# backup
python manage.py dumpdata > backup_data.json
# backup human
python manage.py dumpdata --indent 2 --exclude contenttypes --exclude auth.permission > backup_data.json
# backup spesifik
python manage.py dumpdata scripts > scripts_backup.json
# recover data
python manage.py migrate
python manage.py loaddata backup_data.json
# Backup lengkap dengan timestamp
python manage.py dumpdata --indent 2 --exclude contenttypes --exclude auth.permission > backup_full_$(date +%Y%m%d).json
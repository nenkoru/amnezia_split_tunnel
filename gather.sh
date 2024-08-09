# List of companies
companies=("Facebook" "Google" "Twitter")

# Iterate over each company and execute the command
for company in "${companies[@]}"
do
    echo "Executing command for $company..."
    python3 NetblockTool/NetblockTool.py -v "$company" -o "$company" -s
done

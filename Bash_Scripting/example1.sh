#Gets all file paths without expansion/substitution
read -r -d '' path_param <<'EOF'
PARAMETERS_PATHS_HERE
EOF
read -r -d '' path_exec <<'EOF'
SCRIPT_PATH_HERE
EOF

#Parses all dragged files' paths from Windows paths to unix paths
path_param=$(echo $path_param | tr -d '"' | sed 's/[[:space:]]\([A-Z]:\)/\n\1/g' | 
                                sed 's/[A-Z]:/\/mnt\/\L&/g' | tr '\\' '\/'\');
mapfile -t path_param <<< "$path_param";
path_param=("${path_param[@]//:}");

#Same, but with the .sh script path
path_exec=$(echo $path_exec | sed 's/[[:space:]]\([A-Z]:\)/\n\1/g' | 
                              sed 's/[A-Z]:/\/mnt\/\L&/g' | tr '\\' '\/'\'); 
path_exec="${path_exec//:}";

#Sets working directory to the folder where the script is located
cd "${path_exec%\/*}";

#Executes script with or without parameters
if [[ ${path_param[@]} == "" ]];
    then "$path_exec";
    else "$path_exec" "${path_param[@]/#${path_exec%\/*}\/}";
fi;

#Leaves WSL console open after the .sh script finishes executing (optional)
cd ~; bash;

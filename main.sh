while true
do

bash autoStart.bash
curl -s "https://serverautorestarter.nxsolution.repl.co" >/dev/null 2>&1 && echo "$(date +'%Y%m%d%H%M%S') Keeping online ..." && sleep 60 ## Change this to your URL!
done

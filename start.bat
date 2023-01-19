@ECHO OFF
docker run -dt --name="falconi" --rm --cpus="4.0" --memory-swap=-1 --memory="6g" --network="host" -p 4000:4000 falconi:latest
pause


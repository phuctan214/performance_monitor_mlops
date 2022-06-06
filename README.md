# Performance Monitoring Capstone Project

Detect data drift and real time monitoring loss function 

## How to run an example

Tools:
* `Evidently` - library for the metrics calculations
* `Prometheus` - service to store the metrics
* `Grafana` - service to build the dashboards
* `Docker` - service to rule them all

### You can run experiment in two ways:

#### Run with data which we prepare:

1. **Install Docker** if you haven't used it before.
2. **Build container** using 
```bash
docker compose up
```

3. **Install dependencies**.

- install dependencies
```bash
pip install -r requirements.txt
```

4. **Then run the docker image from the example directory**:
```bash
./example_run_request.py
```

#### Run with your data:
1. **Install Docker** if you haven't used it before.
2. **Build container** using 
```bash
docker compose up
```
3. Prepare your data as dict format and send it via endpoint(http://localhost:8085/iterate/data-car)
![Alt text](/images/example.png?raw=true "Optional Title")

### Dashboard

1. **Explore the dashboard**.
 
Go to the browser and access the Grafana dashboard at http://localhost:3000. At first, you will be asked for login and password. Both are `admin`. 

To see the monitoring dashboard in the Grafana interface, click "General" and navigate to the chosen dashboard (e.g. "Evidently Data Drift").

![Alt text](/images/dashboard.png?raw=true "Optional Title")

2. **Stop the example**.

To stop the process of sending data, cancel the execution of the example script (press CTRL-C).

If the Docker containers were not stopped after that, run a command:

```bash
docker compose down
```

# BAD PRACTICE: using an ancient, unpatched base image full of CVEs
FROM python:3.6-slim

WORKDIR /app

# BAD PRACTICE: running as root (no non-root user created)

COPY requirements.txt .

# BAD PRACTICE: not pinning pip, not using --no-cache-dir
RUN pip install -r requirements.txt

# BAD PRACTICE: copying everything including tests, secrets, .git etc
COPY . .

# BAD PRACTICE: container runs as root by default
# (no USER instruction)

# BAD PRACTICE: exposes sensitive env var with hardcoded secret in image layer
ENV SECRET_KEY="supersecretpassword123"

EXPOSE 5000

# BAD PRACTICE: running with debug mode on in the container
CMD ["python", "-m", "flask", "--app", "app.main", "run", "--host=0.0.0.0", "--port=5000", "--debug"]

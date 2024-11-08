Для запуску потрібно встановити Rabbitmq - https://www.rabbitmq.com/docs/install-windows (рекомендовано через Chocolatey)<br />
Далі, потрібно додати до Path шляхи C:\Program Files\Erlang OTP\bin та C:\Program Files\RabbitMQ Server\rabbitmq_server-4.0.2\sbin (за умови дефолтних локацій)<br />
Запускаємо rabbitmq командою rabbitmq-server в окремому терміналі<br />
Відкриваємо окремий термінал і вводимо команду celery -A bloom worker --loglevel=info --pool=solo<br />
Відкриваємо окремий термінал і вводимо команду celery -A bloom beat --loglevel=info<br />

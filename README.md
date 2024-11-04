Для запуску потрібно встановити Rabbitmq - https://www.rabbitmq.com/docs/install-windows (рекомендовано через Chocolatey)
Далі, потрібно додати до Path шляхи C:\Program Files\Erlang OTP\bin та C:\Program Files\RabbitMQ Server\rabbitmq_server-4.0.2\sbin (за умови дефолтних локацій)
Запускаємо rabbitmq командою rabbitmq-server в окремому терміналі
Відкриваємо окремий термінал і вводимо команду celery -A bloom worker --loglevel=info --pool=solo
Відкриваємо окремий термінал і вводимо команду celery -A bloom beat --loglevel=info

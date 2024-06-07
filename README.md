# dd CSLP (CyberSecurity Learn Platform)
Платформа для изучения информационной безопасности.
В первую очередь этот проект предназначен для дипломной работы. Разрабатывается dd CSLP для того, чтобы:
- научиться разрабатывать средние по сложности системы, которые легко можно маштабировать;
- при разработке активно использовать системы контроля версий;
- разрабатывать используя подход микросервисвисной архитектуры;
- использовать Docker, Kubernetes;
- научиться использовать практику CI/CD
- использовать свой продукт для тестирования на проникновение и отказоустойчивость


## Структура платформы
По задумке платформа должна состоять из микросервисов, которые можно будет развернуть независимо друг от друга и 
использовать по своему усмотрению.

Микросервисы:

### ddCTF
CTF платформа для добавления разных задач и последующего их решения.

[ddCTF](https://github.com/dobrodelete/)

### ddBlog
Небольшой блог для того, чтобы можно было писать и читать статьи.

[ddBlog](https://github.com/dobrodelete/)

### ddTaskTracker
Трекер задач, куда можно добавлять, удалять или изменять различные задачи для пользователей.

[ddTaskTracker](https://github.com/dobrodelete/)

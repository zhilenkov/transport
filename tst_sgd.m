pkg load linear-algebra

c = [   3, 4, 6;
        2, 9, 1         ]; % матрица стоимостей проезда

a = [30, 50];	% спрос
b = [20, 40, 20]; % предложение

u = [-1; 1];	% начальная точка (часть u)
v = [1; -10; -10];	% начальная точка (часть v)

p = sum(a);	% 0 <= x(i, j) <= p

point = [u; v]; % переменная, которая понадобится для запоминания стох. градиента на предыдущем шаге, на этапе тестирования хранит начальную точку

iter = 1;

function [res, grad, sgrad] = dualf(c, u, v, a, b, p, t=0.5, prevgrad)

        % Функция возвращает
        % res -- значение функции в точке [u; v]
        % grad -- градиент
        % sgrad -- взвешанный градиент относительно градиента на предыдущем шаге prevgrad, с параметром t
        % Параметры функции
        % с -- матрица стоимостей
        % a -- спрос
        % b -- предложение
        % [u, v] -- начальная точка
        % p = sum(a) -- ограничение сверху по x (прямым переменным)
        % t -- параметр-вес для изменения стохастического градиента
        % prevgrad -- стохастический градиент на предыдущем шаге

        grad = [-a'; -b']; % В случае, когда все значения (c(i, j) + u(i) + v(j)) > 0 это градиент

        r = u + v'; % Выбираем случаи, когда в целевой функции есть слагаемые (c(i, j) + u(i) + v(j)) < 0
        r += c;
        boolr = r < 0;

        res = r .* boolr * p; % Подсчёт значения функции в точке [u; v]
        res = sum(sum(res));
        res -= (a*u + b*v);

        i = sum(p * boolr, 2); % пересчитываем компоненты градиента, если в матрице boolr нашлись ненулевые элементы
        j = sum(p * boolr)';
        vect = [i; j];
        m = randi([1, rows(i)], 1);
        n = randi([1, rows(j)], 1);
        
        chooser = [];
        
        proxmat = cartprod(1:length(i), 1:length(j));
        for counter = 1:rows(proxmat)
            if r(proxmat(counter, :)(1), proxmat(counter, :)(2)) < 0
                chooser = [chooser; proxmat(counter, :)];
            endif
        endfor
        
        ch = rows(chooser);
        if ch > 0
            ch = randi([1, ch])
        endif
        
        sgrad = grad; 

        grad = grad + vect;
        
        if ch > 0
            is = zeros(rows(i), 1); 
            js = zeros(rows(j), 1); 

            is(chooser(ch, 1)) += p; 
            js(chooser(ch, 2)) += p; 

            sgrad = t*prevgrad + (1 - t)*(sgrad + [is; js]);
        endif
        
        pres = [grad, sgrad]
        
endfunction

mat = [];
[result, grad, sgrad] = dualf(c, u, v, a, b, p, t=0, point);
point += 1/(6*iter)*sgrad;
u = point(1:2);
v = point(3:end);

while iter < 300 
    [result, grad, sgrad] = dualf(c, u, v, a, b, p, t=0, sgrad);
    point += 1/(iter)*sgrad;
    u = point(1:2);
    v = point(3:end);
    iter += 1;
    printf("result = %f, norm = %f, iter = %d\n",result, norm(point), iter);
    mat = [mat; result, iter];
endwhile

dlmwrite("data.csv", mat, ",")

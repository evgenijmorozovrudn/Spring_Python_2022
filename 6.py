#!/usr/bin/env python
# coding: utf-8

# Задача 1. Четные индексы

# In[1]:


print(' '.join(list(input().split())[::2]))


# Задача 2. Наибольший элемент и его индекс

# In[2]:


inp_list = list(enumerate(input().split()))
print(' '.join(map(str, max(inp_list, key = lambda x : x[1])))[::-1])


# Задача 3. Вывести в обратном порядке

# In[4]:


print(input()[::-1])


# Задача 4. Переставить соседние

# In[5]:


lst = list(input().split())
lst[:-1:2], lst[1::2] = lst[1::2], lst[:-1:2]
print(' '.join(lst))


# Задача 5. Циклический сдвиг вправо

# In[6]:


lst = list(input().split())
print(' '.join([lst[-1]] + lst[:-1]))


# Задача 6. Удалить элемент

# In[7]:


lst = list(input().split())
lst.pop(int(input()))
print(' '.join(lst))


# Задача 7. Вставить элемент

# In[9]:


lst = list((input().split()))
n, elem = map(int, input().split())
print(' '.join(map(str, lst[:n] + list([elem]) + lst[n:])))


# In[ ]:


Задача 8. Большой сдвиг


# In[10]:


lst = list(input().split())
print(' '.join(map(str, map(lambda i : ' '.join(lst[-int(i):]) + ' ' + ' '.join(lst[:-int(i)]), input()))))


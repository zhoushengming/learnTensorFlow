import tensorflow as tf

'''
tensorFlow 

Variable 变量
constant 常量

'''

state = tf.Variable(0, name='counter')
print(state.name)

one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)  # 更新变量

init = tf.global_variables_initializer()  # initialize_all_variables

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

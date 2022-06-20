<template>
    <body id="bg">

        <el-alert
            v-if="type === 'success'"
            title="注册成功"
            type="success"
            effect="dark">
        </el-alert>

        <el-alert
            v-if="type === 'error'"
            :title="msg"
            type="error"
            effect="dark">
        </el-alert>

        <el-form :model="ruleForm" class="login-container" :rules="rules" ref="ruleForm" label-position="left" label-width="0px">
           
            <h3 class="title">系统注册</h3>
            <el-form-item>
                <el-input type="text" v-model="ruleForm.userName" placeholder="账号"></el-input>
            </el-form-item>

            <el-form-item prop="userPassword" >
                <el-input type="password" v-model="ruleForm.userPassword" placeholder="密码"></el-input>
            </el-form-item>

            <el-form-item prop="userEmail" required>
                <el-input v-model="ruleForm.userEmail" placeholder="邮箱"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" style="width: 100%;background: #3b3d45;border: none" v-on:click="register">注册</el-button>
            </el-form-item>

        </el-form>
    </body>
</template>

<style scoped>

.login-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 140px auto;
    padding: 35px 35px 15px 35px;
    width: 400px;
    background: rgb(255, 255, 255);
    border: 1px solid;
    box-shadow: 0 0 25px #333131;
}

.title {
    text-align: center;
    padding-bottom: 20px;
    color: #333131;
}

#bg {
    background: url("../../assets/loginbg.jpg") center no-repeat ;
    background-size: cover;
    position: fixed;
    height: 100%;
    width: 100%;
}

body {
    margin: 0px;
}

</style>

<script>

export default {
    name: 'Register',
    data() {
        // 邮箱校验
        var checkEmail = (rule, value, callback) => {
            const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
            if (!value) {
                return callback(new Error('邮箱不能为空'))
            }
            setTimeout(() => {
                if (mailReg.test(value)) {
                    callback()
                } else {
                    callback(new Error('请输入正确的邮箱格式'))
                }
            }, 100)
        }
        // 密码校验
          var checkPassword = (rule, value, callback) => {
            if (!value) {
                return callback(new Error('密码不能为空'))
            }
        }
        return {
            responseResult: [],
            type: 'null',
            msg: '',
            ruleForm: {
                userName: '',
                userPassword: '',
                userEmail: ''
            },
            rules: {
                userEmail: [
                    { validator: checkEmail, trigger: 'blur' }
                ],
                userPassword: [
                    { validator: checkPassword, trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
        register() {
            var _this = this        // 变量中转 vuex接收不到this
            this.$axios
            .post('/register', {
                username: this.ruleForm.userName,
                password: this.ruleForm.userPassword,
                email: this.ruleForm.userEmail
            })
            .then((sucessResponse) => {
                console.log(sucessResponse.data);
                if (sucessResponse.data.code == 200) {
                    _this.type = 'success'  // 显示注册成功的消息
                    setTimeout(3000)
                    _this.$router.push({path : '/login'})    // 跳转到登录页面
                } else {
                    _this.type = 'error'
                    _this.msg = sucessResponse.data.message
                }
            }).catch((failResponse) => {
                
            });
        }
    },
}

</script>


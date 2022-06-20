<template>
    <body id="bg">
            <el-form class="login-container" label-position="left" label-width="0px">
            <h3 class="title">系统登录</h3>
            <el-form-item>
                <el-input type="text" v-model="loginForm.username" placeholder="账号"></el-input>
            </el-form-item>

            <el-form-item>
                <el-input type="password" v-model="loginForm.password" placeholder="密码"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" style="width: 100%;background: #3b3d45;border: none" v-on:click="login">登录</el-button>
            </el-form-item>

            <el-form-item>
                <router-link to="/register">
                    <el-button type="primary" style="width: 100%;background: #3b3d45;border: none">注册</el-button>
                </router-link>
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
    name: 'Login',
    data() {
        return {
            loginForm: {
                username: '',
                password: ''
            },
            responseResult: []
        }
    },
    methods: {
        login () {
            var _this = this
            console.log(this.$store.state)
            this.$axios
                .post('/login', {
                    username: this.loginForm.username,
                    password: this.loginForm.password
                })
                .then(successResponse => {
                    // console.log(successResponse.data);
                if (successResponse.data.code == 200) {
                    // var data = this.loginForm
                    _this.$store.commit('login', _this.loginForm)
                    _this.$router.push({path : '/index'})    // 跳转到主页
                    console.log(successResponse.data);
                }
                })
                .catch(failResponse => {
                })
        }

    }    
}

</script>


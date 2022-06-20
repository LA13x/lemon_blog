<template>
    <div class="articles-area">
        <el-card style="text-align: left">
            <div v-for="article in articles" :key="article.id" class="articleItem">
                <div >
                    <router-link class="article-link" :to="{path:'blog/article',query:{id: article.id}}"><span style="font-size: 20px;"><strong>{{article.title}}</strong></span></router-link>
                    <el-divider content-position="left">{{ article.username }}</el-divider>
                    <router-link class="article-link" :to="{path:'blog/article',query:{id: article.id}}"><p>{{article.abstract}}</p></router-link>
                </div>
                <el-divider content-position="right">{{ article.date }}</el-divider>
            </div>
            <el-pagination
            background
            layout="total, prev, pager, next, jumper"
            @current-change="handleCurrentChange"
            :page-size="pageSize"
            :total="total"
            style="padding-left: 33%">
            </el-pagination>
        </el-card>
    </div>
</template>

<script>
  export default {
    data () {
      return {
        imgURL: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        username: window.localStorage.getItem('user'),
        cal: new Date(),
        articles: [],
        pageSize: 6,
        total: 0
      }
    },
    mounted() {
        this.loadArticles()
    },
    methods: {
        loadArticles() {
            var _this = this

            // 获取当前用户的文章总数
            this.$axios.get('/get/articles')
            .then((resp) => {
                console.log(resp.data);       
                if(resp.data.code == 200) {
                    _this.total = parseInt(resp.data.article_numbers)
                } else {
                    console.log('请求文章总数出错');
                }
            }).catch((err) => {
                
            });
            
            // 获取所有用户第一页的文章数据
            this.$axios.get('/get/articles/1')
            .then((resp) => {
                console.log(resp.data);       
                if(resp.data.code == 200) {
                    // 获取文章列表
                    _this.articles = resp.data['articles']
                    console.log(_this.articles)
                } else {
                    console.log('请求文章列表出错');
                }
            }).catch((err) => {
                
            });
        },
        handleCurrentChange(page) {
            var _this = this
            this.$axios.get('/get/articles/' + page)
            .then((resp) => {
                console.log(resp.data);       
                if(resp.data.code == 200) {
                    // 获取文章列表
                    _this.articles = resp.data['articles']
                }
            }).catch((err) => {
                
            });
        },
    }
  }
</script>

<style scoped>

    .articles-area {
        width: 990px;
        height: 750px;
        margin-left: auto;
        margin-right: auto;
    }

    .article-link {
        text-decoration: none;
        color: #606266;
    }

    .article-link:hover {
        color: #409EFF;
    }

    .articleItem {
        padding: 25px;
    }

</style>
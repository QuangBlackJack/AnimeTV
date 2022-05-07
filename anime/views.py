from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Provider, Category, Movie, episode, Historywatch, Viewer, comment
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.

# before login
class indexclass(View):
    def get(self, request):
        anime = Movie.objects.filter(type="Anime").order_by('-id')[:8]
        cartoon = Movie.objects.filter(type="Cartoon").order_by('-id')[:8]
        drama = Movie.objects.filter(type="Movie").order_by('-id')[:4]
        power = Movie.objects.filter(type="Power").order_by('-id')[:4]
        movie = Movie.objects.all()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        quangcaophim = Movie.objects.all().last()
        context = {"movie": movie, "history": lichsu, "rank": rank, "qc": quangcaophim, "anime": anime, "cartoon": cartoon, "drama": drama, "power": power}

        return render(request, "homepage.html", context)


class thongtinclass(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank}

        return render(request, "thong-tin-phim.html", context)


class loginclass(View):
    def get(self, request):
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"history": lichsu, "rank": rank}

        return render(request, "dang-nhap.html", context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse("ko co user nao nhu the")
        else:
            anime = Movie.objects.filter(type="Anime").order_by('-id')[:8]
            movie = Movie.objects.all()
            lichsu = Historywatch.objects.order_by('-id')[:3]
            rank = Movie.objects.order_by('-views')[:5]
            quangcaophim = Movie.objects.all().last()
            context = {"movie": movie, "history": lichsu, "rank": rank, "qc": quangcaophim, "anime": anime}

            return render(request, "user-homepage.html", context)


        # return render(request, "dang-nhap.html", context)



class signupclass(View):
    def get(self, request):
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"history": lichsu, "rank": rank}

        return render(request, "dang-ki.html", context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        day = request.POST.get("day")
        month = request.POST.get("month")
        year = request.POST.get("year")
        sex = request.POST.get("sex")
        new_user = Viewer(username=username, password=password, repassword=repassword, email=email, fullname=fullname,
                        day=day, month=month, year=year, sex=sex)
        account = User.objects.create_user(username, email, password)
        if password != repassword:
            return HttpResponse("có mỗi cái password mà nhập lại cũng ko đúng")
        else:
            new_user.save()
            account.save()
            lichsu = Historywatch.objects.order_by('-id')[:3]
            rank = Movie.objects.order_by('-views')[:5]
            context = {"history": lichsu, "rank": rank}

            return render(request, "dang-ki.html", context)

class watchingclass(View):
    def get(self, request, movie_id, ):
        movie = Movie.objects.get(pk=movie_id)
        cm = comment.objects.all()
        movie.views = movie.views + 1
        movie.save()
        eps = episode.objects.all()
        history = Historywatch(movieName=movie.movieName, picture=movie.picture)
        history.save()
        context = {"eps": eps, "movie": movie, "cm": cm}

        return render(request, "xem-phim.html", context)


class continueswatchingclass(View):
    def get(self, request, episode_id, ):
        cm = comment.objects.all()
        movie = episode.objects.get(pk=episode_id)
        eps = episode.objects.all()
        context = {"eps": eps, "movie": movie, "cm": cm}

        return render(request, "xem-phim-theo-tap.html", context)

class animeClass(View):
    def get(self, request):
        movie = Movie.objects.filter(type="Anime").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title}

        return render(request, "theo-the-loai.html", context)


class cartoonClass(View):
    def get(self, request):
        movie = Movie.objects.filter(type="Cartoon").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title}

        return render(request, "theo-the-loai.html", context)


class dramaClass(View):
    def get(self, request):
        movie = Movie.objects.filter(type="Movie").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title}

        return render(request, "theo-the-loai.html", context)



class superClass(View):
    def get(self, request):
        movie = Movie.objects.filter(type="Power").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title}

        return render(request, "theo-the-loai.html", context)








# after login

class userindexclass(View):

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse("ko co user nao nhu the")
        else:
            user = User.objects.get(username=username)
            anime = Movie.objects.filter(type="Anime").order_by('-id')[:8]
            cartoon = Movie.objects.filter(type="Cartoon").order_by('-id')[:8]
            drama = Movie.objects.filter(type="Movie").order_by('-id')[:4]
            power = Movie.objects.filter(type="Power").order_by('-id')[:4]
            movie = Movie.objects.all()
            lichsu = Historywatch.objects.order_by('-id')[:3]
            rank = Movie.objects.order_by('-views')[:5]
            quangcaophim = Movie.objects.all().last()
            context = {"movie": movie, "history": lichsu, "rank": rank, "qc": quangcaophim, "anime": anime, "cartoon": cartoon, "drama": drama, "power": power, "user": user}

            return render(request, "user-homepage.html", context)


class userindexclasss(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        anime = Movie.objects.filter(type="Anime").order_by('-id')[:8]
        cartoon = Movie.objects.filter(type="Cartoon").order_by('-id')[:8]
        drama = Movie.objects.filter(type="Movie").order_by('-id')[:4]
        power = Movie.objects.filter(type="Power").order_by('-id')[:4]
        movie = Movie.objects.all()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        quangcaophim = Movie.objects.all().last()
        context = {"movie": movie, "history": lichsu, "rank": rank, "qc": quangcaophim, "anime": anime, "cartoon": cartoon, "drama": drama, "power": power, "user": user}

        return render(request, "user-home-pagee.html", context)

class userthongtinclass(View):
    def get(self, request,user_id ,movie_id):
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.get(pk=movie_id)
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "user": user}

        return render(request, "user-thong-tin-phim.html", context)

class userwatchingclass(View):
    def get(self, request, movie_id, user_id):
        cm = comment.objects.all()
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.get(pk=movie_id)
        movie.views = movie.views + 1
        movie.save()
        eps = episode.objects.all()
        history = Historywatch(movieName=movie.movieName, picture=movie.picture)
        history.save()
        context = {"eps": eps, "movie": movie, "user": user, "cm": cm}

        return render(request, "user-xem-phim.html", context)

    def post(self, request, user_id, movie_id):
        message = request.POST.get("message")
        cm = comment.objects.all()
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.get(pk=movie_id)
        movie.views = movie.views + 1
        movie.save()
        eps = episode.objects.all()
        history = Historywatch(movieName=movie.movieName, picture=movie.picture)
        history.save()
        speech = comment(username=user.username, message=message, movieName=movie.movieName)
        speech.save()
        context = {"eps": eps, "movie": movie, "user": user, "cm": cm}

        return render(request, "user-xem-phim.html", context)

class usercontinueswatchingclass(View):
    def get(self, request, episode_id, user_id):
        cm = comment.objects.all()
        user = User.objects.get(pk=user_id)
        movie = episode.objects.get(pk=episode_id)
        eps = episode.objects.all()
        context = {"eps": eps, "movie": movie, "user": user, "cm": cm}

        return render(request, "user-xem-phim-theo-tap.html", context)

    def post(self, request, user_id, episode_id):
        message = request.POST.get("message")
        cm = comment.objects.all()
        user = User.objects.get(pk=user_id)
        movie = episode.objects.get(pk=episode_id)
        eps = episode.objects.all()
        speech = comment(username=user.username, message=message, movieName=movie.movieName)
        speech.save()
        context = {"eps": eps, "movie": movie, "user": user, "cm": cm}

        return render(request, "user-xem-phim-theo-tap.html", context)



class useranimeClass(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.filter(type="Anime").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title, "user": user}

        return render(request, "user-theo-the-loai.html", context)


class usercartoonClass(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.filter(type="Cartoon").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title, "user": user}

        return render(request, "user-theo-the-loai.html", context)


class userdramaClass(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.filter(type="Movie").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title, "user": user}

        return render(request, "user-theo-the-loai.html", context)



class usersuperClass(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.filter(type="Power").order_by('-id')
        title = movie.all().last()
        lichsu = Historywatch.objects.order_by('-id')[:3]
        rank = Movie.objects.order_by('-views')[:5]
        context = {"movie": movie, "history": lichsu, "rank": rank, "title": title, "user": user}

        return render(request, "user-theo-the-loai.html", context)









# test
def test(request):
    movie = Movie.objects.all()
    #cm = comment.objects.all()
    context = {"movie": movie}

    return render(request, "test.html", context)
    #return HttpResponse(cm.message)



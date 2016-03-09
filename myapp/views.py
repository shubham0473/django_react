import requests
from django.conf import settings
from django.utils.safestring import mark_safe
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
import json
# import simplejson
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from models import *
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import JsonResponse
# from jsonify.decorators import ajax_request
# try:
# from django.utils import simplejson
# except:
#     import simplejson as json

ADMIN = 0
STUDENT = 1
FACULTY = 2

# Create your views here.

def home(request):
	print "Here in home "
	return render(request, "gentelella/index.html")

@ensure_csrf_cookie
def login(request):
	print "Here in Login!!!"
	if request.method == 'POST':
		print "yaha aaya !! "
		json_data = request.body
		# print request.body
		if not json_data:
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		json_data = json.loads(json_data)
		print json_data
		email_ = json_data['email']
		pwd = json_data['password']
		# print email_, pwd
		user = MyUser.objects.get(email = email_)
		print "IN LOGIN"
		print user and user.check_password(pwd)
		# print make_password(pwd)
		if user and user.check_password(pwd):
			request.session['id'] = user.user_id
			# print request.session
			print "In profile redirect"
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/profile/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			print "IN login wala !! "
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
			return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET':
		print "get h"
		return render(request,'maggulater/login.html')


def faculty(request):
	if 'id' in request.session.keys():
		print "faculty_id" , request.session['id']
	if request.method == 'GET':
		return render(request, 'maggulater/faculty.html')

def signUp(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		name = json_data['name']
		email = json_data['email']
		link_to_dp = "link"
		type_flag = json_data['flag']
		dob = json_data['dob']
		password = json_data['password']
		user = MyUser(name = name, email = email, link_to_dp = link_to_dp , type_flag = type_flag , dob = dob)
		hashed_pass = user.make_password(password)
		print hashed_pass
		print type_flag
		user.set_password(hashed_pass)
		user.save()
		user = MyUser.objects.get(email = email)
		# duser = User.objects.create_user(name,email,password)
		if type_flag == FACULTY:
			newfac = Faculty(Faculty_Id = user)
			newfac.save()
		elif type_flag == ADMIN:
			newadm = Admin(Admin_Id = user)
			newadm.save()
		elif type_flag == STUDENT:
			print "student"
			print user.user_id
			newst = Student(Student_Id = user)
			newst.save()
		print "Created Users succesfully"
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
		return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET':
		return render(request, 'maggulater/signup.html')


def profile(request):
	if 'id' in request.session.keys():
		print "user_id" , request.session['id']
		user = MyUser.objects.get(user_id = request.session['id'])
		if user.type_flag == ADMIN:
			print "ADMIN"
			return render(request, "maggulater/admin.html")
		if user.type_flag == STUDENT:
			print "STUDENT"
			return render(request, "maggulater/student.html")
		if user.type_flag == FACULTY:
			print "FACULTY"
			return render(request, "maggulater/faculty.html")
	else :
		return redirect('/login/')


def studenthome(request):
	print "student_id" , request.session['id']
	return render(request , 'maggulater/student.html')


def adminhome(request):
	print "admin_id" , request.session['id']
	return render(request , 'maggulater/admin.html')

def index2(request):
	# print "admin_id" , request.session['id']
	return render(request , 'gentelella/index2.html')

def parentPortal(request):
	if request.method == 'POST' :
		json_data = request.body
		if not json_data :
			print ("Error !! No credentials Given !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/parentPortal/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		json_data = json.loads(json_data)
		_email = json_data['Email']
		user = MyUser.objects.get(email = email_)
		if user is None or user.email != _email :
			print("Sorry Wrong Credentials !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/parentPortal/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			Performance = Performance_Sheet.objects.get(Student_Id = user)
			return render(request , 'maggulater/Parent_Portal.html')


def forgotPassword(request):
	if request.method == 'POST' :
		json_data = request.body
		if not json_data :
			print ("Error !! No credentials Given !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/forgotPassword/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		json_data = json.loads(json_data)
		_email = json_data['email']
		name = json_data['name']
		user = MyUser.objects.get(email = _email)
		if user is None or user.name != name :
			print("Sorry Wrong Credentials !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/forgotPassword/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			newpassword = json_data['password']
			hashed_pass = user.make_password(newpassword)
			user.set_password(hashed_pass)
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
			print response
			# return HttpResponseRedirect(("/login/"))
			return HttpResponse(json.dumps(response), content_type ='application/json')
	if request.method == 'GET' :
		return render(request, 'maggulater/forgotPassword.html')


def logout(request):
	try:
		del request.session['id']
	except KeyError:
		pass
	print request.session
	return render(request,'maggulater/login.html')


def searchcourse(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/searchcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['course_id']

		course = Course.objects.get(course_id = cid)

		if course:
			request.session['course_id'] = cid
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/searchcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET':
		return render(request , 'maggulater/student_home.html')

# API for enrolling a student in a course
def enroll(request):
	newenroll = Enrolls(student_id = request.session['id'],course_id = request.session['course_id'])
	newenroll.save()
	response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
	return HttpResponse(json.dumps(response), content_type='application/json')


# API to add a new notice
def addnotice(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/addnotice/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['c_id']
		msg = json_data['message']

		newnotice = Notice(timestamp = now(), message = msg, c_id = cid)
		newnotice.save()
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
		return HttpResponse(json.dumps(response), content_type='application/json')


# API to add a new course
def addcourse(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/searchcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['c_id']
		cname = json_data['course_name']
		pre = json_data['prereq']
		fac_id = request.session['id']
		course = Course.objects.get(course_id = cid)

		if course:
			perror("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/addcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')

		newcourse = Course(course_id = cid,course_name = cname,prereq = pre,faculty = fac_id)
		newcourse.save()
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/facultyhome/'}
		return HttpResponse(json.dumps(response), content_type='application/json')


# API to approve a course
def approve(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'approve'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['c_id']

		course = Course.objects.get(course_id = cid)

		if course:
			course.approve()
			response = {'status': 1, 'message': "Confirmed!!", 'url':'coursehome'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			perror("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'error'}
			return HttpResponse(json.dumps(response), content_type='application/json')


# API to get list of all courses
def allcourses(request):
	j = Course.objects.all()
	return HttpResponse([i.serialize() for i in j])


# API to get list of all courses of a faculty
def allfacultycourses(request):
	j = Course.objects.all()
	d = [i.serialize() for i in j if i.faculty_id == request.session['id']]
	return HttpResponse(d)

# API to get list of all courses of a faculty
def allstudentcourses(request):
	enrolled_courses = []
	print request.session['id']
	for c in Enrolls.objects.all():
		print c.student_id.Student_Id.user_id
		if c.student_id.Student_Id.user_id == request.session['id']:
			p = c.course_id.course_id
			enrolled_courses.append(p)
	print enrolled_courses
	d = [i.serialize() for i in Course.objects.all() if i.course_id in enrolled_courses]
	print d
	return HttpResponse(d)

# API to get all notices
def allnotices(request):
	for i in Notice.objects.all():
		print i.serialize
	return jsonify(json_data = [i.serialize for i in Notice.objects.all()])


# API to get all notices of a course
def allcoursenotices(request):
	return jsonify(json_data = [i.serialize for i in Notice.objects.get(c_id = request.session['course_id']).all()])


# API to get all notices of a student
def allstudentnotices(request):
	enrolled_courses = []
	for c in Enrolls.objects.get(student_id = request.session['id']).all(request):
		p = c.course_id
		enrolled_courses.append(p)

	d = jsonify(json_data = [i.serialize for i in Notice.objects.all() if i.c_id in enrolled_courses])
	return d


# API for listing
def listcourses(request):
	return render(request, 'maggulater/course_list.html')

# API for listing
def listfacultycourses(request):
	return render(request, 'maggulater/faculty_course_list.html')

# API for listing
def liststudentcourses(request):
	return render(request, 'maggulater/student_course_list.html')

# API for adding a lecture
def addLecture(request):
	if request.method == 'POST' :
		json_data = request.body
		print json_data
		json_data = json.loads(json_data)
		# course_id = request.session['course_id']
		course_id = 1
		print json_data
		notes = json_data['Notes']
		Date_Time = json_data['Date_Time']
		date = datetime.datetime.strptime(Date_Time, '%Y-%m-%d').date()
		Topic = json_data['Topic']
		Link = json_data['Link']
		print "Here!!"
		course = Course.objects.get(course_id = course_id)
		NewLec = Lecture(Course_Id = course,Topic =  Topic)
		print "here"
		NewLec.setDate(date)
		NewLec.setNotes(notes)
		NewLec.setLink(Link)
		NewLec.save()
		Lecture_Id= NewLec.Lecture_Id
		Questions = json_data['Questions']
		Answers = json_data['Answers']
		NewTest = Test(Lecture_Id = NewLec)
		NewTest.setQuestions(Questions)
		NewTest.setAnswers(Answers)
		NewTest.save()
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
		return HttpResponse(json.dumps(response), content_type='application/json')
	if request.method == 'GET' :
		return render(request, 'maggulater/addLecture.html')


def json_response(something=None):
    return HttpResponse(
        json.dumps(something),
        content_type='application/json; charset=UTF-8')


def render_to_react_string(component_name, ctx=None):
    if ctx is None:
        ctx = {}

    try:
        response = requests.get(settings.NODE_SERVER,
                            params={'component_name': component_name, 'data': json.dumps(ctx)})

        if response.status_code == requests.codes.ok:
            return mark_safe(response.text)
        else:
            return ''
    except Exception as exc:
        print exc
        return ''


def get_comments():
    return list(Comment.objects.values('id', 'name', 'text'))


def load_comments(request):
    return json_response({"comments": get_comments()})


def post_comment(request):
    Comment.objects.create(name=request.POST['name'], text=request.POST['text'])
    return json_response({"success": True})


def index(request):

    return render(request, 'index.html')

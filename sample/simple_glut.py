from OpenGL.GLUT import *
import sys
import simple_renderer

def reshape_func(w, h):
	sumple_renderer.resize(w, h == 0 and 1 or h)

def disp_func():
	simple_renderer.draw()
	glutSwapBuffers()

if __name__=="__main__":
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(256, 256)
	glutCreateWindow(b"triangle")
	glutDisplayFunc(disp_func)
	glutIdleFunc(disp_func)
	glutReshapeFunc(reshape_func)

	simple_renderer.initialize()

	glutMainLoop()

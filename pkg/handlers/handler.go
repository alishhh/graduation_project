package handler

import "github.com/gin-gonic/gin"

type Handler struct {
}

func (h *Handler) InitRouters() *gin.Engine {
	router := gin.New()

	auth := router.Group("/auth")
	{
		auth.POST("sign-up", h.signUp)
		auth.POST("sign-in", h.signIn)
	}

	api := router.Group("/api")
	{
		lits := api.Group("/users")
		{
			lits.POST("/", h.createUser)
			lits.GET("/", h.getAllUsers)
			lits.GET("/:id", h.getUserById)
			lits.PUT("/:id", h.updateUser)
			lits.DELETE("/:id", h.deleteUser)

			items := lits.Group(":id/doctors")
			{
				items.POST("/", h.createDoctor)
				items.GET("/", h.getAllDoctors)
				items.GET("/:id", h.getDoctorById)
				items.PUT("/:id", h.updateDoctor)
				items.DELETE("/:id", h.deleteDoctor)
			}
		}
	}

	return router
}

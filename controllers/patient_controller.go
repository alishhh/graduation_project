package controllers

import (
	"net/http"

	"dariger.kz/models"
	"dariger.kz/services"
	"github.com/gin-gonic/gin"
)

type PatientController struct {
	PatientService services.PatientService
}

func New(patientservice services.PatientService) PatientController {
	return PatientController{
		PatientService: patientservice,
	}
}

func (pc *PatientController) CreatePatient(ctx *gin.Context) {
	var patient models.Patient
	if err := ctx.ShouldBindJSON(&patient); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}
	err := pc.PatientService.CreatePatient(&patient)
	if err != nil {
		ctx.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"message": "success"})
}

func (pc *PatientController) GetPatient(ctx *gin.Context) {
	email := ctx.Param("email")
	patient, err := pc.PatientService.GetPatient(&email)
	if err != nil {
		ctx.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, patient)
}

func (pc *PatientController) GetAll(ctx *gin.Context) {
	patients, err := pc.PatientService.GetAll()
	if err != nil {
		ctx.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, patients)
}

func (pc *PatientController) UpdatePatient(ctx *gin.Context) {
	var patient models.Patient
	if err := ctx.ShouldBindJSON(&patient); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}
	err := pc.PatientService.UpdatePatient(&patient)
	if err != nil {
		ctx.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"messgae": "success"})
}

func (pc *PatientController) DeletePatient(ctx *gin.Context) {
	email := ctx.Param("email")
	err := pc.PatientService.DeletePatient(&email)
	if err != nil {
		ctx.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"message": "success"})
}

func (pc *PatientController) RegisterPatientRoutes(rg *gin.RouterGroup) {
	route := rg.Group("/patient")
	route.POST("/create", pc.CreatePatient)
	route.GET("/get/:email", pc.GetPatient)
	route.GET("/getall", pc.GetAll)
	route.PATCH("/update", pc.UpdatePatient)
	route.DELETE("/delete/:email", pc.DeletePatient)
}

package main

import (
	"context"
	"fmt"
	"log"

	"dariger.kz/controllers"
	"dariger.kz/services"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
)

var (
	server            *gin.Engine
	patientservice    services.PatientService
	patientcontroller controllers.PatientController
	ctx               context.Context
	patientcollection *mongo.Collection
	mongoclient       *mongo.Client
	err               error
)

func init() {
	ctx = context.TODO()

	mongoconnection := options.Client().ApplyURI("mongodb://localhost:27017")
	mongoclient, err = mongo.Connect(ctx, mongoconnection)
	if err != nil {
		log.Fatal(err)
	}
	err = mongoclient.Ping(ctx, readpref.Primary())
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Mongo connection established")

	patientcollection = mongoclient.Database("patientdb").Collection("patients")
	patientservice = services.NewPatientService(patientcollection, ctx)
	patientcontroller = controllers.New(patientservice)
	server = gin.Default()
}

//v1/patient/create
func main() {
	defer mongoclient.Disconnect(ctx)

	basepath := server.Group("/v1")
	patientcontroller.RegisterPatientRoutes(basepath)

	log.Fatal(server.Run(":9090"))
}

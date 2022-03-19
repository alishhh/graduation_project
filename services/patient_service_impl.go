package services

import (
	"context"
	"errors"

	"dariger.kz/models"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

type PatientServiceImpl struct {
	patientcollection *mongo.Collection
	ctx               context.Context
}

func NewPatientService(patientcollection *mongo.Collection, ctx context.Context) PatientService {
	return &PatientServiceImpl{
		patientcollection: patientcollection,
		ctx:               ctx,
	}
}

func (p *PatientServiceImpl) CreatePatient(patient *models.Patient) error {
	_, err := p.patientcollection.InsertOne(p.ctx, patient)
	return err
}

func (p *PatientServiceImpl) GetPatient(email *string) (*models.Patient, error) {
	var patient *models.Patient
	query := bson.D{bson.E{Key: "email", Value: email}}
	err := p.patientcollection.FindOne(p.ctx, query).Decode(*patient)
	return patient, err
}

func (p *PatientServiceImpl) GetAll() ([]*models.Patient, error) {
	var patients []*models.Patient
	cursor, err := p.patientcollection.Find(p.ctx, bson.D{{}})
	if err != nil {
		return nil, err
	}
	for cursor.Next(p.ctx) {
		var patient models.Patient
		err := cursor.Decode(&patient)
		if err != nil {
			return nil, err
		}
		patients = append(patients, &patient)
	}

	if err := cursor.Err(); err != nil {
		return nil, err
	}

	cursor.Close(p.ctx)

	if len(patients) == 0 {
		return nil, errors.New("Documents not found")
	}
	return nil, nil
}

func (p *PatientServiceImpl) UpdatePatient(patient *models.Patient) error {
	filter := bson.D{bson.E{Key: "email", Value: patient.Email}}
	update := bson.D{bson.E{Key: "$set", Value: bson.D{bson.E{Key: "email", Value: patient.Email},
		bson.E{Key: "password", Value: patient.Password},
		bson.E{Key: "firstname", Value: patient.Firstname},
		bson.E{Key: "lastname", Value: patient.Lastname},
		bson.E{Key: "phone_number", Value: patient.Phone_number},
		bson.E{Key: "region", Value: patient.Region}}}}
	//bson.E{Key: "created_at", Value: patient.Created_at},
	//bson.E{Key: "updated_at", Value: patient.Updated_at},
	//bson.E{Key: "deleted_at", Value: patient.Deleted_at}}}}
	result, _ := p.patientcollection.UpdateOne(p.ctx, filter, update)
	if result.MatchedCount != 1 {
		return errors.New("No matched document found for update")
	}
	return nil
}

func (p *PatientServiceImpl) DeletePatient(email *string) error {
	filter := bson.D{bson.E{Key: "email", Value: email}}
	result, _ := p.patientcollection.DeleteOne(p.ctx, filter)
	if result.DeletedCount != 1 {
		return errors.New("No matched document found for delete")
	}
	return nil
}

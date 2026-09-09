export type BookingStatus =
  | "pending"
  | "confirmed"
  | "in_progress"
  | "quality_check"
  | "completed"
  | "cancelled";

export type ServiceLocation =
  | "workshop"
  | "home_service";

export interface BookingCreate {
  customer_name: string;
  whatsapp: string;
  vehicle_category: string;
  vehicle_type: string;
  vehicle_model: string;
  plate_number: string;
  service_location: ServiceLocation;
  services: string[];
  preferred_date: string;
  time_slot: string;
  address?: string;
  notes?: string;
  estimated_total: number;
}

export interface Booking extends BookingCreate {
  id: string;
  code: string;
  status: BookingStatus;
  created_at: string;
  updated_at: string;
}

export interface BookingMeta {
  today: string;
  workshop_name: string;
}
